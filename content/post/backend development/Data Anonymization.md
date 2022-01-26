---
title: "Data Anonymization"
draft: true
---



See

-  [Guide to Anonymization](https://iapp.org/media/pdf/resource_center/Guide_to_Anonymisation.pdf)

# Domain vocabulary

- Data anonymization inverse of : Data disclosure, identification
- Data protection
- Anonymization policy (strategy / technique ?)



## Anonymization techniques

- **Attribute suppression** : database column removal
- **Record suppression** : useful to remove outliers in a set
- **character / data masking** : e.g. 'xxxxxxxx@gmail.com' : 
  -  creating a mirror image of a database and implementing alteration strategies, such as character shuffling, encryption, term, or character substitution
  - preserve or not length of original data
- **Pseudonymization** :
  - Pseudonymization is a data de-identification tool that substitutes private identifiers with false identifiers or pseudonyms, such as swapping the “John Smith” identifier with the “Mark Spencer” identifier
  - It maintains statistical precision and data confidentiality, allowing changed data to be used for creation, training, testing, and analysis, while at the same time maintaining data privacy
  - generator should be random and ideally not reused for different attributes
- **Generalization** :
  - Generalization involves excluding some data purposely to make it less identifiable. Data may be modified into a series of ranges or a large region with reasonable boundaries
  - e.g. : from 23 to 20-30
- **Data swapping** : permutation / shuffling of database records. Switching attributes (columns) that include recognizable values, such as date of birth, can make a huge impact on anonymization
- **Data perturbation** : typically round values and introduce random noise. The base should be defined with care so as to be efficient while making the dataset still analysable
- **Synthetic data** 

