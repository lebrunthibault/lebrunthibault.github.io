## The Challenge of Complexity

- When complexity gets out of hand, developers can no longer understand the software well enough to change or extend it easily and safely. On the other hand, a good design can create opportunities to exploit those complex features

Requisite for a good modeling

- Design is iterative : [XP](https://www.agilealliance.org/glossary/xp/)
  - Extreme Programming recognizes the importance of design decisions, but it strongly resists upfront design. Instead, it puts an admirable effort into communication and improving the project's ability to change course rapidly. With that ability to react, developers can use the "simplest thing that could work" at any stage of a project and then continuously refactor, making many small design improvements, ultimately arriving at a design that fits the customer's true needs.
  - This book intertwines design and development practice and illustrates how domain-driven design and Agile development reinforce each other
  - A sophisticated approach to domain modeling within the context of an Agile development process will accelerate development. The interrelationship of process with domain development makes this approach more practical than any treatment of "pure" design in a vacuum
- Developer and domain experts have a close relationship

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220505081918292.png?token=GHSAT0AAAAAABPCLTQJU6CCH6ENNF4AN3M4YTWEZCQ" alt="image-20220505081918292" style="zoom:80%;" />



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220505082237100.png?token=GHSAT0AAAAAABPCLTQIXTFW2HSZTWQNEYD4YTWE2FQ" alt="image-20220505082237100" style="zoom:80%;" />



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

This model-based communication is not limited to diagrams in Unified Modeling Language (UML). To make most effective use of a model, it needs to pervade every medium of communication. It increases the utility of written text documents, as well as the informal diagrams and casual conversation reemphasized in Agile processes. It improves communication through the code itself and through the tests for that code. The use of language on a project is subtle but all-important...

## Ubiquitous Language

- To create a supple, knowledge-rich design calls for a versatile, shared team language, and a lively experimentation with language that seldom happens on software projects
- A project faces serious problems when its language is fractured. Domain experts use their jargon while technical team members have their own language tuned for discussing the domain in terms of design
- The terminology of day-to-day discussions is disconnected from the terminology embedded in the code (ultimately the most important product of a software project). And even the same person uses different language in speech and in writing, so that the most incisive expressions of the domain often emerge in a transient form that is never captured in the code or even in writing
- **Translation blunts communication and makes knowledge crunching anemic**.
- Yet none of these dialects can be a common language because none serves all needs.
- The vocabulary of that UBIQUITOUS LANGUAGE includes the names of classes and prominent operations. The LANGUAGE includes terms to discuss rules that have been made explicit in the model. It is supplemented with terms from high-level organizing principles imposed on the model (such as CONTEXT MAPS and large-scale structures, which will be discussed in Chapters 14 and 16). Finally, this language is enriched with the names of patterns the team commonly applies to the domain model
- The meanings of words and phrases echo the semantics of the model.
- Persistent use of the UBIQUITOUS LANGUAGE will force the model's weaknesses into the open. The team will experiment and find alternatives to awkward terms or combinations
- Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code. Use the same language in diagrams, writing, and especially speech.
- Iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model. Resolve confusion over terms in conversation, in just the way we come to agree on the meaning of ordinary words.
- Recognize that a change in the UBIQUITOUS LANGUAGE is a change to the model.
- Domain experts should object to terms or structures that are awkward or inadequate.

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
- A document shouldn't try to do what the code already does well, other **documents need to illuminate meaning, to give insight into large-scale structures, and to focus attention on core elements**

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

# Chapter Three. Binding Model and Implementation

## Model-Driven Design

- many complex projects do attempt some sort of domain model, but they don't maintain a tight connection between the model and the code. The model they develop, possibly useful as an exploratory tool at the outset, becomes increasingly irrelevant and even misleading
- Many design methodologies advocate an analysis model, quite distinct from the design and usually developed by different people different from the software implentation. It is meant as a tool for understanding only; mixing in implementation concerns is thought to muddy the waters
- The result is that pure analysis models get abandoned soon after coding starts, and most of the ground has to be covered again
- If the managers perceive analysis to be a separate process, the development team may not be given adequate access to domain experts
- If the design, or some central part of it, does not map to the domain model, that model is of little value, and the correctness of the software is suspect. At the same time, complex mappings between models and design functions are difficult to understand and, in practice, impossible to maintain as the design changes. A deadly divide opens between analysis and design so that insight gained in each of those activities does not feed into the other.
- MODEL-DRIVEN DESIGN discards the dichotomy of analysis model and design to search out a single model that serves both purposes.
- Design a portion of the software system to reflect the domain model in a very literal way, so that mapping is obvious. Revisit the model and modify it to be implemented more naturally in software, even as you seek to make it reflect deeper insight into the domain. Demand a single model that serves both purposes well, in addition to supporting a robust UBIQUITOUS LANGUAGE.
- Draw from the model the terminology used in the design and the basic assignment of responsibilities. The code becomes an expression of the model, so a change to the code may be a change to the model. Its effect must ripple through the rest of the project's activities accordingly
- To tie the implementation slavishly to a model usually requires software development tools and languages that support a modeling paradigm, such as object-oriented programming.
- model <=> design <=> code

## Modeling Paradigms and Tool Support

- We need to use a modeling paradigm supported by software tools that allow you to create direct analogs to the concepts in the model (OO)

![image-20220507093203297](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507093203297.png?token=AEHIPTJ4X7SW65RMKBZEJVLCOY6NC)

### Example From Procedural to MODEL-DRIVEN

- Using data importer / exporter, repositories, factories and entities
- The MODEL-DRIVEN DESIGN scales easily and can include constraints on combining rules and other enhancements.



## Letting the Bones Show: Why Models Matter to Users

- the system view should be coherent with the model
- example internet explorer favorites stored as filenames : **Quietly changing data is completely unacceptable in most applications.**
- never get different user model and design/implementation model.
- When a design is based on a model that reflects the basic concerns of the users and domain experts, the bones of the design can be revealed to the user to a greater extent than with other design approaches. Revealing the model gives the user more access to the potential of the software and yields consistent, predictable behavior

## Hands-On Modelers

- software development is *all* design
- If the people who write the code do not feel responsible for the model, or don't understand how to make the model work for an application, then the model has nothing to do with the software
- If developers don't realize that changing code changes the model, then their refactoring will weaken the model rather than strengthen it
- Meanwhile, when a modeler is separated from the implementation process, he or she never acquires, or quickly loses, a feel for the constraints of implementation
- The basic constraint of MODEL-DRIVEN DESIGN—that the model supports an effective implementation and abstracts key domain knowledge—is half-gone, and the resulting models will be impractical
- Finally, the knowledge and skills of experienced designers won't be transferred to other developers if the division of labor prevents the kind of collaboration that conveys the subtleties of coding a MODEL-DRIVEN DESIGN.
- The effectiveness of an overall design is very sensitive to the quality and consistency of finegrained design and implementation decisions. With a MODEL-DRIVEN DESIGN, a portion of the code is an expression of the model; changing that code changes the model. Programmers are modelers

![image-20220507153117495](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507153117495.png?token=AEHIPTLUM7624AM5N2CE3S3CO2IQG)

# Part II: The Building Blocks of a Model-Driven Design

- The design style in this book largely follows the principle of "responsibility-driven design," put forward in Wirfs-Brock et al. 1990 and updated in Wirfs-Brock 2003. It also draws heavily (especially in Part III) on the ideas of "design by contract" described in Meyer 1988. It is consistent with the general background of other widely held best practices of object-oriented design, which are described in such books as Larman 1998
- Using standard patterns also adds to the UBIQUITOUS LANGUAGE, which all team members can use to discuss model and design decisions.
- Developing a good domain model is an art. But the practical design and implementation of a model's individual elements can be relatively systematic
- Isolating the domain design from the mass of other concerns in the software system will greatly clarify the design's connection to the mode

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507155029300.png?token=AEHIPTNVERIDZ4JL77CPMPTCO2KYC" alt="image-20220507155029300" style="zoom:80%;" />



# Chapter Four. Isolating the Domain

-  We need to decouple the domain objects from other functions of the system, so we can avoid confusing the domain concepts with other concepts related only to software technology or losing sight of the domain altogether in the mass of the system.

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507155140580.png?token=AEHIPTOJVECEWFFGMXATD4LCO2K4Q" alt="image-20220507155140580" style="zoom:67%;" />

- In an object-oriented program, UI, database, and other support code often gets written directly into the business objects. Additional business logic is embedded in the behavior of UI widgets and data-base scripts. This happens because it is the easiest way to make things work, in the short run
- When the domain-related code is diffused through such a large amount of other code, it becomes extremely difficult to see and to reason about. Superficial changes to the UI can actually change business logic. To change a business rule may require meticulous tracing of UI code, database code, or other program elements. Implementing coherent, model-driven objects becomes impractical. Automated testing is awkward. With all the technologies and logic involved in each activity, a program must be kept very simple or it becomes impossible to understand.
- Creating programs that can handle very complex tasks calls for **separation of concerns**
- The essential principle is that any element of a layer depends only on other elements in the same layer or on elements of the layers "beneath" it. Communication upward must pass through some indirect mechanism, which I'll discuss a little later

### User Interface (or Presentation Layer)

> Responsible for showing information to the user and interpreting the user's commands. The external actor might sometimes be another computer system rather than a human user

#### Application Layer

> - Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems
> - This layer is kept thin. It does not contain business rules or knowledge
> -  It does not have state reflecting the business situation, but it can have state that reflects the progress of a task for the user or the program

#### Domain Layer (or Model Layer)

> Responsible for representing concepts of the business, information about the business situation, and business rules. State that reflects the business situation is controlled and used here

#### Infrastructure Layer

> The infrastructure layer may also support the pattern of interactions between the four layers through an architectural framework.

**Partition a complex program into layers. Develop a design within each layer that is cohesive and that depends only on the layers below. Follow standard architectural patterns to provide loose coupling to the layers above. Concentrate all the code related to the domain model in one layer and isolate it from the user interface, application, and infrastructure code. The domain objects, free of the responsibility of displaying themselves, storing themselves, managing application tasks, and so forth, can be focused on expressing the domain model. This allows a model to evolve to be rich enough and clear enough to capture essential business knowledge and put it to work**

### Relating the Layers

- Layers are meant to be loosely coupled, with design dependencies in only one direction
- But when an object of a lower level needs to communicate upward (beyond answering a direct query), we need another mechanism, drawing on architectural patterns for relating layers such as callbacks or OBSERVERS (Gamma et al. 1995).
- The grandfather of patterns for connecting the UI to the application and domain layers is MODELVIEW-CONTROLLER (MVC)
- But not all infrastructure comes in the form of SERVICES callable from the higher layers. Some technical components are designed to directly support the basic functions of other layers (such as providing an abstract base class for all domain objects) and provide the mechanisms for them to relate (such as implementations of MVC and the like). Such an "architectural framework" has much more impact on the design of the other parts of the program.

### Architectural Framework

- (It may seem counterintuitive for a subclass to be in a layer higher than that of the parent class, but keep in mind which class reflects more knowledge of the other
- Judiciously applying only the most valuable of framework features reduces the coupling of the implementation and the framework, allowing more flexibility in later design decisions.

## The Domain Layer Is Where the Model Lives

- domain-driven design requires only one particular layer to exist.
- Isolating the domain implementation is a prerequisite for domain-driven design.

## The Smart UI "Anti-Pattern"

- If an unsophisticated team with a simple project decides to try a MODEL-DRIVEN DESIGN with LAYERED ARCHITECTURE, it will face a difficult learning curve. Team members will have to master complex new technologies and stumble through the process of learning object modeling (which is challenging, even with the help of this book!). The overhead of managing infrastructure and layers makes very simple tasks take longer. Simple projects come with short time lines and modest expectations

When the project is simple, timeline short, team unexperienced we can consider this pattern :

- Put all the business logic into the user interface. Chop the application into small functions and implement them as separate user interfaces, embedding the business rules into them. Use a relational database as a shared repository of the data. Use the most automated UI building and visual programming tools available.
- It is a common mistake to undertake a sophisticated design approach that the team isn't committed to carrying all the way through. Another common, costly mistake is to build a complex infrastructure and use industrial-strength tools for a project that doesn't need them

## Other Kinds of Isolation

- "Distillation," discusses how to make distinctions within the domain layer that can unencumber the essential concepts of the domain from peripheral detail
- co-evolving an effective domain model and an expressive implementation

# Chapter Five. A Model Expressed in Software

-  Connecting model and implementation has to be done at the detail level. This chapter focuses on those individual model elements
- This discussion will start with the issues of designing and streamlining (object) associations
- we'll focus on making distinctions among the three patterns of model elements that express the model: ENTITIES, VALUE OBJECTS, and SERVICES.
- Certain distinctions have emerged that clarify the meaning of model elements and tie into a body of design practices for carving out specific kinds of objects
- A SERVICE is something that is done for a client on request. In the technical layers of the software, there are many SERVICES. They emerge in the domain also, when some activity is modeled that corresponds to something the software must do, but does not correspond with state. (Although it is a slight departure from object-oriented modeling tradition)
- The ideas of high cohesion and low coupling, often thought of as technical metrics, can be applied to the concepts themselves. In a MODEL-DRIVEN DESIGN, MODULES are part of the model, and they should reflect concepts in the domain.



## Associations

- The interaction between modeling and implementation is particularly tricky with the associations between objects. 
- For every traversable association in the model, there is a mechanism in the software with the same properties.
- The design has to specify a particular traversal mechanism whose behavior is consistent with the association in the model.

There are at least three ways of making associations more tractable.

- Imposing a traversal direction
-  Adding a qualifier, effectively reducing multiplicity
- Eliminating nonessential associations
- It is important to constrain relationships as much as possible. A bidirectional association means that both objects can be understood only together. When application requirements do not call for traversal in both directions, adding a traversal direction reduces interdependence and simplifies the design. Understanding the domain may reveal a natural directional bias.

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507163326663.png?token=AEHIPTKDYF72SJJHKNP6CKLCO2PZE" alt="image-20220507163326663" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220507163417259.png?token=AEHIPTJFYIRYONII7AEWSJ3CO2P4K" alt="image-20220507163417259" style="zoom:67%;" />

- Constraining the traversal direction of a many-to-many association effectively reduces its implementation to one-to-many—a much easier design.
- Consistently constraining associations in ways that reflect the bias of the domain not only makes those associations more communicative and simpler to implement, it also gives significance to the remaining bidirectional associations
- as constraints on associations are discovered they should be included in the model and implementation. They make the model more precise and the implementation easier to maintain.
- Carefully distilling and constraining the model's associations will take you a long way toward a MODEL-DRIVEN DESIGN.

## Entities (a.k.a. Reference Objects)

- Many objects are not fundamentally defined by their attributes, but rather by a thread of continuity and identity.
- A person has an identity that stretches from birth to death and even beyond. That person's physical attributes transform and ultimately disappear
- Am I the same person I was at age five? This kind of metaphysical question is important in the search for effective domain models. Slightly rephrased: Does the user of the application care if I am the same person I was at age five?
- Some objects are not defined primarily by their attributes. They represent a thread of identity that runs through time and often across distinct representations. Sometimes such an object must be matched with another object even though attributes differ. An object must be distinguished from other objects even though they might have the same attributes. Mistaken identity can lead to data corruption.
-  Identity is a subtle and meaningful attribute of ENTITIES, which can't be turned over to the automatic features of the language (e.g. a software object might be an entity for a JRE but is not necessarily an entity in the domain even though it has an object id)
- In fact, two objects can have the same identity without having the same attributes or even, necessarily, being of the same class
- When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model. Keep the class definition simple and focused on life cycle continuity and identity. Define a means of distinguishing each object regardless of its form or history. Be alert to requirements that call for matching objects by attributes. Define an operation that is guaranteed to produce a unique result for each object, possibly by attaching a symbol that is guaranteed unique. This means of identification may come from the outside, or it may be an arbitrary identifier created by and for the system, but it must correspond to the identity distinctions in the model. **The model must define what it means to be the same thing.**
- Example of seats in an event (can be or not entities with number identifiers)

### Modeling ENTITIES

- Beyond identity issues, ENTITIES tend to fulfill their responsibilities by coordinating the operations of objects they own
- Because in this example project the phone and address are used to query a unique customer we put them in the Customer entity



<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220508090403447.png?token=AEHIPTK7DFW3KCVKB7NJBKLCO6D4C" alt="image-20220508090403447" style="zoom:67%;" />

#### Designing the Identity Operation

- Sometimes certain data attributes, or combinations of attributes, can be guaranteed or simply constrained to be unique within the system
- When there is no true unique key made up of the attributes of an object, another common solution is to attach to each instance a symbol (such as a number or a string) that is unique within the class. Once this ID symbol is created and stored as an attribute of the ENTITY, it is designated immutable. It must never change, even if the development system is unable to directly enforce this rule
- Often the ID is generated automatically by the system. The generation algorithm must guarantee uniqueness within the system, which can be a challenge with concurrent processing and in distributed systems
- Often, the means of identification demand a careful study of the domain, as well.
- When I book airline tickets or reserve a hotel, I'm given confirmation numbers that are unique identifiers for the transaction
- In some cases, the uniqueness of the ID must apply beyond the computer system's boundaries (exchange record across different systems)
- **This is why identity-assigning operations often involve human input**. Checkbook reconciliation software, for instance, may offer likely matches, but the user is expected to make the final determination.

## Value Objects

- Many objects have no conceptual identity. These objects describe some characteristic of a thing.
- Tracking the identity of ENTITIES is essential, but attaching identity to other objects can hurt system performance, add analytical work, and muddle the model by making all objects look the same.
- Software design is a constant battle with complexity. We must make distinctions so that special handling is applied only where necessary.
- However, if we think of this category of object as just the absence of identity, we haven't added much to our toolbox or vocabulary. In fact, these objects have characteristics of their own and their own significance to the model. These are the objects that describe things.
- VALUE OBJECTS are instantiated to represent elements of the design that we care about only for what they are, not who or which they are.
- VALUE OBJECTS can even reference ENTITIES
- VALUE OBJECTS are often passed as parameters in messages between objects. They are frequently transient, created for an operation and then discarded.
- When you care only about the attributes of an element of the model, classify it as a VALUE OBJECT. Make it express the meaning of the attributes it conveys and give it related functionality. Treat the VALUE OBJECT as immutable. Don't give it any identity and avoid the design complexities necessary to maintain ENTITIES.

### Designing VALUE OBJECTS

- If two people have the same name, that does not make them the same person, or make them interchangeable. But the object representing the name is interchangeable, because only the spelling of the name matters. A Name object can be copied from the first Person object to the second.
- In fact, the two Person objects might not need their own name instances. The same Name object could be shared between the two Person objects (each with a pointer to the same name instance) with no change in their behavior or identity. That is, their behavior will be correct until some change is made to the name of one person. Then the other person's name would change also! To protect against this, in order for an object to be shared safely, it must be immutable: it cannot be changed except by full replacement.
- The same issues arise when an object passes one of its attributes to another object as an argument or return value. Anything could happen to the wandering object while it is out of control of its owner. The VALUE could be changed in a way that corrupts the owner, by violating the owner's invariants. This problem is avoided either by making the passed object immutable, or by passing a copy.
- Optimization trick : flyweight to share a single instance of a value objects everywhere

Sharing is best restricted to those cases in which it is most valuable and least troublesome:

- When saving space or object count in the database is critical
- When communication overhead is low (such as in a centralized server) (NB: not a distributed one)
- When the shared object is strictly immutable
- Some concepts (entity, value object, immutability) cannot be declared in a language (but are present in the model). This can be checked with naming conventions, selective documentation, and *lots of discussion* 
- As long as a VALUE OBJECT is immutable, change management is simple—there isn't any change except full replacement

### Special Cases: When to Allow Mutability

- If the VALUE changes frequently
- If object creation or deletion is expensive
- If replacement (rather than modification) will disturb clustering (as discussed in the previous example)
- If there is not much sharing of VALUES, or if such sharing is forgone to improve clustering or for some other technical reason
- Just to reiterate: If a VALUE's implementation is to be mutable, then it must not be shared. Whether you will be sharing or not, design VALUE OBJECTS as immutable when you can.

### Example Tuning a Database with VALUE OBJECTS

- Some database uses a copy of each VO instead of immutable reference in a technique called *denormalization* and is often used when access time is more critical than storage space or simplicity of maintenance
- In a relational database, you might want to put a particular VALUE in the table of the ENTITY that owns it, rather than creating an association to a separate table.
- We can freely make these copies because we are dealing with VALUE OBJECTS.
