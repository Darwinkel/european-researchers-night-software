# European Researcher's Night Software


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
- I have to come up with a novel short story, similar to, but not based on, existing stories
- I suggest a "random" shuffle of the sentences
  - The system also generates a true random shuffle
- I am provided with some unbiased, nonsuggestive random examples
- I am provided with some random suggestions for themes or subjects
- I can optionally leave my sex and age demographics before AND after the survey
- 