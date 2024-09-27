"""Reconstruct text using an OpenAPI-compatible server."""

from openai import OpenAI

from ern.settings import env


def dutch_chat(sentences: str) -> list[dict[str, str]]:
    """Chatbot conversation in Dutch."""
    return [
        {
            "role": "system",
            "content": "Je bent een intelligente taalkundige en "
            "een expert in het herstellen van foutief geordende tekst.",
        },
        {
            "role": "user",
            "content": f"Herschik de volgende lijst door de zinnen te verplaatsen, "
            f"waarbij je de zinnen zelf niet veranderd en geen extra opmerkingen maakt: {sentences}",
        },
    ]


def english_chat(sentences: str) -> list[dict[str, str]]:
    """Chatbot conversation in English."""
    return [
        {
            "role": "system",
            "content": "You are an intelligent linguist and expert at restoring wrongly ordered text.",
        },
        {
            "role": "user",
            "content": f"Rearrange the following list by moving the sentences, "
            f"where you do not modify the sentences themselves and don't make any additional comments: {sentences}",
        },
    ]


def reconstruct_with_llm(lang: str, human_shuffled_story: str, random_shuffled_story: str) -> tuple[str, str]:
    """Reconstruct text using a language model."""
    if lang == "nl":
        model = "BramVanroy/GEITje-7B-ultra"
        client = OpenAI(base_url=f"{env("OPENAPI_HOST")}:8891/v1", api_key="asdf")
        reconstruct_human_shuffle_chat = dutch_chat(human_shuffled_story)
        reconstruct_random_shuffle_chat = dutch_chat(random_shuffled_story)

    else:
        model = "microsoft/Phi-3.5-mini-instruct"
        client = OpenAI(base_url=f"{env("OPENAPI_HOST")}:8890/v1", api_key="asdf")
        reconstruct_human_shuffle_chat = english_chat(human_shuffled_story)
        reconstruct_random_shuffle_chat = english_chat(random_shuffled_story)

    llm_reconstructed_human_story = client.chat.completions.create(
        model=model, messages=reconstruct_human_shuffle_chat, temperature=0.7
    )

    llm_reconstructed_random_story = client.chat.completions.create(
        model=model, messages=reconstruct_random_shuffle_chat, temperature=0.7
    )

    print(reconstruct_human_shuffle_chat)
    print(llm_reconstructed_human_story)

    print(reconstruct_random_shuffle_chat)
    print(llm_reconstructed_random_story)

    return (
        llm_reconstructed_human_story.choices[0].message.content,
        llm_reconstructed_random_story.choices[0].message.content,
    )
