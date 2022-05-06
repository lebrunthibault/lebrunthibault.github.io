## The Challenge of Complexity

- When complexity gets out of hand, developers can no longer understand the software well enough to change or extend it easily and safely. On the other hand, a good design can create opportunities to exploit those complex features

Requisite for a good modeling

- Design is iterative : [XP](https://www.agilealliance.org/glossary/xp/)
  - Extreme Programming recognizes the importance of design decisions, but it strongly resists upfront design. Instead, it puts an admirable effort into communication and improving the project's ability to change course rapidly. With that ability to react, developers can use the "simplest thing that could work" at any stage of a project and then continuously refactor, making many small design improvements, ultimately arriving at a design that fits the customer's true needs.
  - This book intertwines design and development practice and illustrates how domain-driven design and Agile development reinforce each other
  - A sophisticated approach to domain modeling within the context of an Agile development process will accelerate development. The interrelationship of process with domain development makes this approach more practical than any treatment of "pure" design in a vacuum
- Developer and domain experts have a close relationship

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220505081918292.png?token=AEHIPTKRCK2UT6TMN5TEN23COOEMI" alt="image-20220505081918292" style="zoom:80%;" />



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220505082237100.png?token=AEHIPTKURI4LRADE7F5GDRTCOOEYS" alt="image-20220505082237100" style="zoom:80%;" />



# Part I: Putting the Domain Model to Work

- Every software program relates to some activity or interest of its user. That subject area to which the user applies the program is the domain of the software
- A model is a selectively simplified and consciously structured form of knowledge. An appropriate model makes sense of information and focuses it on a problem
- A domain model is not a particular diagram; it is the idea that the diagram is intended to convey
- *it is a rigorously organized and selective abstraction of that knowledge.*

## The Utility of a Model in Domain-Driven Design

In domain-driven design, three basic uses determine the choice of a model.

- The model and the heart of the design shape each other : **domain <-> implementation**
- The model is the backbone of a language used by all team members
- The model is distilled knowledge

### The Heart of Software

- The heart of software is its ability to solve domain-related problems for its user
-  leaders within a team who understand the centrality of the domain can put their software project back on course when development of a model that reflects deep understanding gets lost in the shuffle

# Chapter One. Crunching Knowledge

-  I wrote a very simple prototype, driven by an automated test framework. I avoided all infrastructure. There was no persistence, and no user interface (UI)

## Ingredients of Effective Modeling

- Binding the model and the implementation (prototyping)
- Cultivating a language based on the model
- Developing a knowledge-rich model (The objects had behavior and enforced rules. The model wasn't just a data schema)
- Distilling the model : iteration, adding and dropping model concepts
- Brainstorming and experimenting: natural language make good concepts appear

**It is the creativity of brainstorming and massive experimentation, leveraged through a model based language and disciplined by the feedback loop through implementation, that makes it possible to find a knowledge-rich model and distill it. This kind of knowledge crunching turns the knowledge of the team into valuable models**



## Knowledge Crunching

- It comes in the form of documents written for the project or used in the business, and lots and lots of talk
- Early versions or prototypes feed experience back into the team and change interpretations.
- Knowledge should trickle in both direction to take advantage of feedback and enrichment
- Other projects use an iterative process, but they fail to build up knowledge because they don't abstract. Useful software can be built that way, but the project will never arrive at a point where powerful new features unfold as corollaries to older features
- Good programmers will naturally start to abstract and develop a model that can do more work. But when this happens only in a technical setting, without collaboration with domain experts, the concepts are naive. That shallowness of knowledge produces software that does a basic job but lacks a deep connection to the domain expert's way of thinking.

## Continuous Learning

- *When we set out to write software, we never know enough*. we don't realize how much we don't know
- Meanwhile, all projects leak knowledge: people move on, stuff is out sourced (giving code but not knowledge)
- Highly productive teams grow their knowledge consciously, practicing continuous learning (Kerievsky 2003). For developers, this means improving technical knowledge, along with general domain-modeling skills (such as those in this book). But it also includes serious learning about the specific domain they are working in

## Knowledge-Rich Design

- Domain experts are usually not aware of how complex their mental processes are as, in the course of their work, they navigate all these rules, reconcile contradictions, and fill in gaps with common sense. Software can't do this
- Extracting the cargo booking policy to a specific class (strategy) not because it's gonna change but because it's clearer.
- Know when to do this kind of things (not always). Comes with model distillation

## Deep Models

- Knowledge crunching is an exploration, and you can't know where you will end up.

# Chapter Two. Communication and the Use of Language

This model-based communication is not limited to diagrams in Unified Modeling Language (UML). To make most effective use of a model, it needs to pervade every medium of communication. It increases the utility of written text documents, as well as the informal diagrams and casual conversation reemphasized in Agile processes. It improves communication through the code itself and through.

The tests for that code. The use of language on a project is subtle but all-important...

## Ubiquitous Language

- To create a supple, knowledge-rich design calls for a versatile, shared team language, and a lively experimentation with language that seldom happens on software projects
- A project faces serious problems when its language is fractured. Domain experts use their jargon while technical team members have their own language tuned for discussing the domain in terms of design
- The terminology of day-to-day discussions is disconnected from the terminology embedded in the code (ultimately the most important product of a software project). And even the same person uses different language in speech and in writing, so that the most incisive expressions of the domain often emerge in a transient form that is never captured in the code or even in writing
- Translation blunts communication and makes knowledge crunching anemic.
- Yet none of these dialects can be a common language because none serves all needs.
- The vocabulary of that UBIQUITOUS LANGUAGE includes the names of classes and prominent operations. The LANGUAGE includes terms to discuss rules that have been made explicit in the model. It is supplemented with terms from high-level organizing principles imposed on the model (such as CONTEXT MAPS and large-scale structures, which will be discussed in Chapters 14 and 16). Finally, this language is enriched with the names of patterns the team commonly applies to the domain model
- The meanings of words and phrases echo the semantics of the model.
- Persistent use of the UBIQUITOUS LANGUAGE will force the model's weaknesses into the open. The team will experiment and find alternatives to awkward terms or combinations
- Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code. Use the same language in diagrams, writing, and especially speech.
- Iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model. Resolve confusion over terms in conversation, in just the way we come to agree on the meaning of ordinary words.
- Recognize that a change in the UBIQUITOUS LANGUAGE is a change to the model.
- Domain experts should object to terms or structures that are awkward or inadequate to

## Modeling Out Loud

- Play with the model as you talk about the system. Describe scenarios out loud using the elements and interactions of the model, combining concepts in ways allowed by the model. Find easier ways to say what you need to say, and then take those new ideas back down to the diagrams and code.

## One Team, One Language

- If sophisticated domain experts don't understand the model, there is something wrong with the model.
- The domain experts can use the language of the model in writing use cases, and can work even more directly with the model by specifying acceptance tests
- user and dev jargons  are **extensions** to the language. These dialects should not contain alternative vocabularies for the same domain that reflect distinct models.

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220505091743765.png?token=AEHIPTNAFLQAUDDYBWL6KKDCOOLHK" alt="image-20220505091743765" style="zoom:67%;" />

## Documents and Diagrams

- Simple, informal UML diagrams can anchor a discussion. Sketch a diagram of three to five objects central to the issue at hand, and everyone can stay focused
- UML can be too detailed, schemas should be kept simple
- UML doesn't show behavior, constraints and assertions
- a UML diagram cannot convey two of the most important aspects of a model: the meaning of the concepts it represents, and what the objects are meant to do
- Good diagrams are minimal, show design constraints, but they are not design specifications in every detail. They represent the skeletons of ideas
- **Rather than a diagram annotated with text, I write a text document illustrated with selective and simplified diagrams.**
- **Always remember that the model is not the diagram**



### Written Design Documents

- Once a document takes on a persistent form, it often loses its connection with the flow of the project

#### Documents Should Complement Code and Speech

- Extreme Programming advocates using no extra design documents at all and letting the code speak for itself. Running code doesn't lie, as any other document might. The behavior of running code is unambiguous.
- Extreme Programming concentrates exclusively on the active elements of a program and executable tests. comments and documents fall out of sync
- but documenting exclusively through code has some of the same basic problems as using comprehensive UML diagrams
- A document shouldn't try to do what the code already does well, other documents need to illuminate meaning, to give insight into large-scale structures, and to focus attention on core elements

#### Documents Should Work for a Living and Stay Current

- If a document is outdated (model, ubiquitous language), sometimes it should just be archived (or deleted)
-  Let the UBIQUITOUS LANGUAGE and its evolution be your guide to choosing documents that live and get woven into the project's activity.

### Executable Bedrock

- let's examine XP methods to don't write documentation
  - not always clear to read code (variable names may not be model ones)
  - It takes fastidiousness to write code that doesn't just do the right thing but also says the right thing
- To communicate effectively, the code must be based on the same language used to write the requirements—the same language that the developers speak with each other and with domain experts

## Explanatory Models

- it may aid learning to have other views, used only as educational tools, to communicate general knowledge of the domain
- One particular reason that other models are needed is scope
- Explanatory models offer the freedom to create much more communicative styles tailored to a particular topic
- It is actually helpful to avoid UML in these models, to avoid any false impression of correspondence with the software design