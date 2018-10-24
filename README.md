# Twitter Bot
Emily Fan, Spring 2018 VCG Dev.

### Description

Today, around 15% of Twitter, or 48 million accounts, are bots (CNBC)! From more helpful bots like sports score reporters to the more notorious use of propaganda machines in the recent U.S. election, bots have taken on new roles influencing society on cultural, economic and political levels. This project describes how I created a full scale Twitter Bot. I'll go through how to generate original sentences and post tweets to a public account.

### Timeline
**TODO**: Create a table outlining what you're going to work on step by step.

| # | Description   | Hours Estimated | Completion Date | Miscellaneous |
| - | ------------- | --------------- | --------------- | ------------- |
| 1 | Set up Diffbot API account for parsing and cleaning text | 2 Hours | 8/12/2018 |  |
| 2 | Design Python approach for tokenizing corpus text and create Markov map of text | 3 Hours | 8/19/2018 | Take some time to learn dictionary and list iteration in Python |
| 3 | Write iteration code to perform random walk of Markov map to generate random sentence | 2 Hours | 8/23/2018 |  |
| 4 | Configure Twitter API tokens and write methods to post tweet to account | 2 Hours | 9/06/2018 | Get used to Twitter API |
| 5 | Use Flask and Heroku to create website allowing users to generate and post random tweets on their own. | 5-6 Hours | 9/13/2018 | Read Flask and Heroku documentation |

### Technical Stack
**TODO**: Describe the languages, libraries, frameworks, and tools that went into your project. Make sure to add a brief description of its utility, unlike the list below.

* Python
* Heroku
* Twitter API
* Diffbot API
* Atom

### Implementation
**TODO**: Complete this while you're working on your project. Preferably, you're describing what steps you took for different parts of the project.

* Selecting + Cleaning a Corpus: Visited Project Gutenberg website and downloaded a random novel as a txt file (i.e. Gulliver's Travels, Doctor Doolittle). Used Diffbot to remove extraneous text such as html tags and web formatting from the actual content.
* Generate Markov Chain: Used a loop travel to create a Markov chain map of what the text is supposed to look like. The Markov chain identifies the probability that one word follows another. By performing a random walk of the Markov Chain, I could generate a random sentence.
* Connect with Twitter API: By hooking up the sentence generation functionality with a Twitter account and appropriate tokens, I could post tweets to an account.
* Flask Development: To make this functionality public to other users, I used Flask and Jinja templating to create a website that allows people to interact with the TwitterBot functionality and post tweets they like to the account I created.

### Supplementary Material
**TODO**: Include any links to materials that might help people learn more about your project.

* [Project Presentation](TwitterBot-Deck.pptx)

### Additional Links
* [How to write a good design document](https://medium.freecodecamp.org/how-to-write-a-good-software-design-document-66fcf019569c)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Compilation of Awesome How-To Tutorials](https://github.com/danistefanovic/build-your-own-x)
