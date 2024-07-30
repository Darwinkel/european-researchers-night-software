"""Reconstruct text using an open-source HuggingFace language model."""

from transformers import pipeline


def reconstruct_with_llm(
    lang: str, human_shuffled_story: list[str], random_shuffled_story: list[str]
) -> tuple[str, str]:
    """Reconstruct text using a language model."""
    # load_in_8bit: lower precision but saves a lot of GPU memory
    # device_map=auto: loads the model across multiple GPUs

    if lang == "nl":
        model = "BramVanroy/GEITje-7B-ultra"
        reconstruct_human_shuffle_chat = [
            {
                "role": "system",
                "content": "Je bent een intelligente taalkundige en een expert in het herstellen van foutief geordende tekst.",
            },
            {
                "role": "user",
                "content": f"Herschik de volgende lijst door de zinnen te verplaatsen, waarbij je de zinnen zelf niet veranderd: {human_shuffled_story}",
            },
        ]
        reconstruct_random_shuffle_chat = [
            {
                "role": "system",
                "content": "Je bent een intelligente taalkundige en een expert in het herstellen van foutief geordende tekst.",
            },
            {
                "role": "user",
                "content": f"Herschik de volgende lijst door de zinnen te verplaatsen, waarbij je de zinnen zelf niet veranderd: {random_shuffled_story}",
            },
        ]

    else:
        model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        reconstruct_human_shuffle_chat = [
            {
                "role": "system",
                "content": "You are an intelligent linguist and expert at restoring wrongly ordered text.",
            },
            {
                "role": "user",
                "content": f"Rearrange the following list by moving the sentences, where you do not modify the sentences themselves: {human_shuffled_story}",
            },
        ]
        reconstruct_random_shuffle_chat = [
            {
                "role": "system",
                "content": "You are an intelligent linguist and expert at restoring wrongly ordered text.",
            },
            {
                "role": "user",
                "content": f"Rearrange the following list by moving the sentences, where you do not modify the sentences themselves: {random_shuffled_story}",
            },
        ]

    chatbot = pipeline("text-generation", model=model, model_kwargs={"load_in_4bit": True}, device_map="auto")

    llm_reconstructed_human_story = chatbot(reconstruct_human_shuffle_chat, max_new_tokens=1024)[0]["generated_text"][
        -1
    ]["content"]

    llm_reconstructed_random_story = chatbot(reconstruct_random_shuffle_chat, max_new_tokens=1024)[0]["generated_text"][
        -1
    ]["content"]

    del chatbot
    return llm_reconstructed_human_story, llm_reconstructed_random_story
