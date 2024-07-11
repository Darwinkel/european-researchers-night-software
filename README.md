# European Researcher's Night Software

**Can you out-smart AI?**



## Goal

- Data collection for ERN

## Data collected

- Information about story characteristics by age and sex
- Information about shuffling characteristics by age and sex
- New ground truth Dutch kid’s stories
- Model performance (0-10 rating) on reassembling human shuffle (fluency, logical flow, and factual accuracy)
- Model performance (0-10 rating) on reassembling truly random shuffle (fluency, logical flow, and factual accuracy)

### Open questions
- How to check quality and appropriateness of data? We could do this manually, but depends on the amount of samples we collect. Should not be more than 100 for a single night?

## Tasks

## Scientific considerations
- A confounding variable is the familiarity of LLMs with existing stories
- Language for the experiment and interface is Dutch

## UI/UX
As a user:
- When opening a new session, I have to accept a consent form and select either Dutch or English
- I have to come up with a novel short story, similar to, but not based on, existing stories
- I suggest a "random" shuffle of the sentences
  - The system also generates a true random shuffle
- I am provided with some unbiased, nonsuggestive random ideas for stories
- I am provided with some random suggestions for themes or subjects
- I can optionally leave my sex and age demographics after the survey


### User flow

Every page has a "Stoppen met het experiment" button, which redirects to the first page.

1. First page, the default, shows an explanation of the experiment, and tells users to sign the consent form and select their language
2. User clicks "Volgende"
3. User gets a textbox where they can enter their story. The page shows some suggestions for themes and examples
4. User clicks "Volgende"
5. User sees their story, and can shuffle it. The page shows some examples of shuffles.
6. User clicks "Volgende"
7. User sees the correct story, the human-shuffled story, and the LLM's reconstruction. They can rate the fluency, logical flow, and factual accuracy of the LLM reconstruction
8. User clicks "Volgende"
9. User sees the correct story, the truly randomly shuffled story, and the LLM's reconstruction. They can rate the fluency, logical flow, and factual accuracy of the LLM reconstruction
10. User clicks "Volgende"
11. User enters a thank-you page, with a request for demographics. They can click "Ik wil graag mijn leeftijd en geslacht invullen voor wetenschappelijk onderzoek" or "Nee, bedankt". First button redirects to a page where they can enter it, second button redirects to the first page.

## Data structures

Sample

Age | Sex | Story | Human-shuffled story | Random shuffled story | LLM reconstructed human shuffle | LLM reconstructed random shuffle | Rating of LLM reconstructed human shuffle | Rating of LLM reconstructred random shuffle
