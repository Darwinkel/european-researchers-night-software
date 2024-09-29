"""Reconstruct text using an OpenAI-compatible server."""

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
            f"waarbij je de zinnen zelf niet veranderd, geen extra opmerkingen maakt, geen code schrijft, en geen speciale tekens of opsommingen gebruikt: {sentences}",  # noqa: E501
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
            f"where you do not modify the sentences themselves, don't use special characters, don't write code, and don't make any additional comments or enumerations: {sentences}",  # noqa: E501
        },
    ]


def reconstruct_with_llm(lang: str, human_shuffled_story: str, random_shuffled_story: str) -> tuple[str, str]:
    """Reconstruct text using a language model."""
    if lang == "nl":
        model = env("NL_MODEL")
        client = OpenAI(base_url=env("NL_OPENAI_HOST"), api_key="asdf")
        reconstruct_human_shuffle_chat = dutch_chat(human_shuffled_story)
        reconstruct_random_shuffle_chat = dutch_chat(random_shuffled_story)

    else:
        model = env("EN_MODEL")
        client = OpenAI(base_url=env("EN_OPENAI_HOST"), api_key="asdf")
        reconstruct_human_shuffle_chat = english_chat(human_shuffled_story)
        reconstruct_random_shuffle_chat = english_chat(random_shuffled_story)

    llm_reconstructed_human_story = client.chat.completions.create(
        model=model,
        messages=reconstruct_human_shuffle_chat,  # type: ignore[arg-type]
        temperature=0.7,
    )

    llm_reconstructed_random_story = client.chat.completions.create(
        model=model,
        messages=reconstruct_random_shuffle_chat,  # type: ignore[arg-type]
        temperature=0.7,
    )

    return (
        str(llm_reconstructed_human_story.choices[0].message.content),
        str(llm_reconstructed_random_story.choices[0].message.content),
    )
