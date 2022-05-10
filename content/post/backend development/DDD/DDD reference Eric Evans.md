---
title: "DDD reference"
draft: true

---

book [here](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)

# Definitions 

- domain:  A	 sphere	 of	 knowledge,	 influence,	 or	activity.	The	 subject	area	 to	which	 the	 user	applies	a	 program	is	the	domain	of	the	software
- model:  A	 system	of	 abstractions	 that	 describes	 selected	 aspects	 of	 a	 domain	 and	 can	 be	 used	 to	 solve	problems	related	to	that	domain.
- ubiquitous	language:  A	 language	 structured	 around	 the	 domain	 model	 and	 used	 by	 all	 team	 members	 within	 a	 bounded	context	to	connect	all	the	activities	of	the	team	with	the	software.
- context The	setting	in	which	a	word	or	statement	appears	 that	determines	its	meaning.	Statements	 about	a	model	can	only	be	understood	in	a	context.
- bounded	context A	description	of	a	boundary	 (typically	a	subsystem,	or	the	work	of	a	particular	team)	within	 which	a	particular	model	is	defined	and	applicable.	



# Pattern language overview

<img src="https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220209121827311.png" alt="image-20220209121827311" style="zoom:50%;" />



# 1. Putting	the	Model	to	Work

Domain-Driven	Design	is	an	approach	to	the	development	of	complex	software	in	which	we:

- Focus	on	the	core	domain.
- Explore	 models in	 a	 creative	 collaboration	 of	 domain	 practitioners	 and	software	practitioners.
- Speak	a	ubiquitous	language within	an	explicitly	bounded	context



### Bounded	Context

> NB : in a single unified domain model, we have only one bounded context (ideal but not always realistic, see [this](https://www.culttt.com/2014/11/19/bounded-contexts-context-maps-domain-driven-design))

Explicitly	 define	 the	 context	 within	 which	 a	 model	 applies.	 Explicitly	 set	 boundaries	 in	 terms	 of	 team	 organization,	 usage	 within	 specific	 parts	 of	 the	 application,	 and	 physical	 manifestations	such	as	code	bases	and	database	schemas.	Apply	Continuous	Integration	to	 keep	 model	 concepts	 and	 terms	 strictly	 consistent	 within	 these	 bounds,	 but	 don’t	 be	 distracted	or	confused	by	issues	outside.	Standardize	a	single	development	process	within	 the	context,	which	need	not	be	used	elsewhere.	



### Ubiquitous	Language

Use	the	model	as	the	backbone	of	a	language.	Commit	the team	to	exercising	that	language	 relentlessly	 in	 all	 communication	 within	 the	 team	 and	 in	 the	 code.	 Within	 a	 bounded	 context,	use	the	same	language	in	diagrams,	writing,	and	especially	speech. Recognize	that	a	change	in	the	language	is	a	change	to	the	model. Iron	out	difficulties	by	experimenting	with	alternative	expressions,	which	reflect	alternative	 models.	Then	refactor	the	code,	renaming	classes,	methods,	and	modules	to	conform	to	the	 new	 model.	 Resolve	 confusion	 over	 terms	 in	 conversation,	 in	 just	 the way	 we	 come	 to	 agree	on	the	meaning	of	ordinary	words.



### Continuous	Integration

> Once	a	bounded	context	has	been	defined,	we	must	keep	it	sound.

Institute	a	process	of	merging	all	code	and	other	implementation	artifacts	frequently,	with	 automated	 tests	 to	 flag	 fragmentation	 quickly.	 Relentlessly	 exercise	 the	 ubiquitous	 language	 to	 hammer	 out	a	 shared	 view	 of	 the	model	as	 the	 concepts	 evolve	in	 different	 people’s	heads.



### Model-Driven	Design

> Tightly	 relating	 the	 code	 to	 an	 underlying	 model	 gives	 the	 code	 meaning	 and	 makes	 the	 model	relevant.

Design	a	portion	of	the	software	system	to	reflect	the	domain	model	in	a	very	literal	way,	 so	 that	 mapping	 is	 obvious.	 Revisit	 the	 model	 and	 modify	 it	 to	 be	 implemented	 more	 naturally	in	software,	even	as	you	seek	to	make	it	reflect	deeper	insight	into	the	domain.	 Demand	a	single	model	that	serves	both	purposes	well,	in	addition	to	supporting	a	 fluent	 ubiquitous	language



## Hands-on	Modelers

Any	technical	person	contributing	to	the	model	must	spend	some	time	touching	the	code,	 whatever	 primary	 role	 he	 or	 she	 plays	 on	 the	 project.	 Anyone	 responsible	 for	 changing	 code	must	learn	to	express	a	model	through	the	code.	Every	developer	must	be	involved	in	 some	 level	 of	 discussion	 about	 the	 model	 and	 have	 contact	 with	 domain	 experts.	 Those	 who	contribute	in	different	ways	must	consciously	engage	those	who	touch	the	code	in	a	 dynamic	exchange	of	model	ideas	through	the	ubiquitous	language.	



## Refactoring	Toward	Deeper	Insight

A	model	 that	sloughs	off	the	superficial	and	captures	the	essential	is	a	deep	model

Sophisticated	 domain	 models	 seldom	 turn	 out	 useful	 except	 when	 developed	 through	 an	 iterative	 process	 of	 refactoring,	 including	 close	 involvement	 of	 the	 domain	 experts	 with	 developers	interested	in	learning	about the	domain.



# 2. Building	Blocks	of	a	 Model-Driven	Design



### Layered	Architecture

Isolate	 the	 expression	 of	 the	 domain	 model	 and	 the	 business	 logic,	 and	 eliminate	 any	 dependency	on	infrastructure,	user	interface,	or	even	application	logic	that	is	not	business	 logic.	Partition	a	 complex	program	into	layers.	Develop	a	design	within	 each	layer	 that	is	 cohesive	and	that	depends	only	on	the	layers	below.	Follow	standard	architectural	patterns	 to	 provide	 loose	 coupling	 to	 the	 layers	 above.	 Concentrate	 all	 the	 code	 related	 to	 the	 domain	 model	 in	 one	 layer	 and	 isolate	 it	 from	 the	 user	 interface,	 application,	 and	 infrastructure	code.	The	domain	objects,	free	of	the	responsibility	of	displaying	themselves,	 storing	themselves,	managing	application	tasks,	and	so	forth,	can	be	focused	on	expressing	 the	 domain	model.	This	allows	a	model	 to	 evolve	 to	 be	 rich	 enough	and	 clear	 enough	 to	 capture	essential	business	knowledge	and	put	it	to	work.	

> The	key	goal	here	is	isolation.	Related	patterns,	such	as	“Hexagonal	Architecture”	may	serve	 as	 well	 or	 better	 to	 the	 degree	 that	 they	 allow	 our	 domain	 model	 expressions	 to	 avoid	 dependencies	on	and	references	to	other	system	concerns.



### Entities

- When	an	object	is	distinguished	by	its	identity,	rather	than	its	attributes,	make	this	primary	 to	 its	 definition	 in	 the	 model.	 Keep	 the	 class	 definition	 simple	 and	 focused	 on	 life	 cycle	 continuity	and	identity.
- Define	a	means	of	distinguishing	each	object	 regardless	of	its	 form	or	history.	Be	alert	 to	 requirements	 that	 call	 for	 matching	 objects	 by	 attributes.	 Define	 an	 operation	 that	 is	 guaranteed	to	produce	a	unique	result	for	each	object,	possibly	by	attaching	a	symbol	that	 is	guaranteed	unique.	This	means	of	identification	may	come	from	the	outside,	or	it	may	be	 an	arbitrary	identifier	created	by	and	for	the	system,	but	it	must	correspond	to	the	identity	 distinctions	in	the	model.	
- The	model	must	define	what	it	means	to	be	the	same	thing

> (aka	Reference	Objects)		



### Value	Objects

> Some	objects	describe	or	compute	some	characteristic	of	a	thing.	

When	you	care	only	about	the	attributes	and	logic	of	an	element	of	the	model,	classify	it	as	 a	value	object.	Make	it	express	the	meaning	of	the	attributes	it	conveys	and	give	it	related	 functionality.	 Treat	 the	 value	 object	 as	 immutable.

Make	 all	 operations	 Side-effect-free	 Functions	 that	don’t	depend	on	any	mutable	state.	Don’t	give	a	value	object	any	identity	 and	avoid	the	design	complexities	necessary	to	maintain	entities.	



### Domain	Events

> Something	happened	that	domain experts	care	about.

Model	information	about	activity	in	 the	 domain	as	a	 series	 of	 discrete	 events.	Represent	 each	event	as	a	domain	object.	These	are	distinct	 from	system	events	that	reflect	activity	 within	 the	 software	 itself,	 although	 often	 a	 system	 event	 is	 associated	 with	 a	 domain	 event,	either	as	part	of	a	response	to	the	domain	event	or	as	a	way	of	carrying	information	 about	the	domain	event	into	the	system.

A	domain	event	is	a	full-fledged	part	of	the	domain	model,	a	representation	of	something	 that	happened	in	 the	domain.	Ignore	irrelevant	domain	activity	while	making	 explicit	 the	 events	 that	 the	 domain	 experts	 want	 to	 track or	 be	 notified	 of,	 or	 which	 are	 associated	 with	state	change	in	the	other	model	objects.

Domain	events	are	 ordinarily	 immutable,	as	 they	are	a	 record	 of	 something	 in	 the	 past.	In	 addition	to	a	description	of	the	event,	a	domain	event	typically	contains	a	timestamp	for	the	 time	 the	 event	 occurred and	 the	 identity	 of	 entities	 involved	 in	 the	 event.	 Also,	 a	 domain	 event	often	has	a	separate	timestamp	indicating	when	the	event	was	entered	into	the	system	 and	the	identity	of	the	person	who	entered	it.	When	useful,	an	identity	for	the	domain	event	 can	be	based	on	some	set	of	these	properties.	So,	for	example,	if	two	instances	of	the	same	 event	arrive	at	a	node	they	can	be	recognized as	the	same.



### Services

> Sometimes,	it	just	isn’t	a	thing.

When	a	significant	process	or	transformation	in	the	domain	is	not	a	natural	responsibility	 of	 an	 entity	 or	 value	 object,	 add	 an	 operation	 to	 the	 model	 as	 a	 standalone	 interface	 declared	as	a	service.	Define	a	service	contract,	a	set	of	assertions	about	interactions	with	 the	service.	(See	assertions.)	State	these	assertions	in	the	ubiquitous	language	of	a	specific	 bounded	 context.	 Give	 the	 service	 a	 name,	 which	 also	 becomes	 part	 of	 the	 ubiquitous	 language.



### Modules

> NB : a bounded context is composed of several modules

- There	is	a	limit	to	how	many	things	a	 person	can	 think	about	at	once	 (hence	low	coupling)
- Incoherent	 fragments	of	ideas	are	as	 hard	to	understand	as	an	undifferentiated	soup	of	ideas	(hence	high	cohesion).

Choose	modules	 that	 tell	 the	story	of	 the	system	and	contain	a	cohesive	set	of	concepts.	 Give	the modules	names	that	become	part	of	the	ubiquitous	language.	Modules	are	part	of	 the	model	and	their	names	should	reflect	insight	into	the	domain

This	often	yields	low	coupling	between	modules,	but	if	it	doesn’t	look	for	a	way	to	change	 the	model	to	disentangle	the	concepts,	or	an	overlooked	concept	that	might	be	the	basis	of	 a	module	that	would	bring	the	elements	together	in	a	meaningful	way.	Seek	low	coupling	 in	the	sense	of	concepts	that	can	be	understood	and	reasoned	about	independently.	Refine	 the	model	until	it	partitions	according	to	high-level	domain	concepts	and	the	corresponding	 code	is	decoupled	as	well.

> (aka Packages)



### Aggregates

Cluster	the	entities	and	value	objects	into	aggregates	and	define	boundaries	around	each.	 Choose	 one	 entity	 to	 be	 the	 root	 of	 each	 aggregate,	 and	 allow	 external	 objects	 to	 hold	 references	 to	 the	 root	 only	 (references	 to	 internal	members	 passed	 out	 for	 use	 within	 a	 single	operation	only).	Define	properties	and	invariants	 for	 the	aggregate	as	a	whole	and	 give	enforcement	responsibility	to	the	root	or	some	designated	framework	mechanism.

- Within	 an	 aggregate	 boundary,	 apply	 consistency	 rules	 synchronously.	 Across	 boundaries,	 handle	updates	asynchronously. (NB : by using domain events ?)
- different aggregates can be distributed



### Repositories

> Query	access	to	aggregates	expressed	in	the	ubiquitous	language.

For	each	type of	aggregate	that	needs	global	access,	create	a	service	that	can	provide	the	 illusion	of	an	in-memory	collection	of	all	objects	of	that	aggregate’s	root	type.	Set	up	access	 through	a	well-known	global	interface.	Provide	methods	to	add	and	remove	objects,	which	 will	encapsulate	the	actual	insertion	or	removal	of	data	in	the	data	store.	Provide	methods	 that	 select	 objects	 based	 on	 criteria	 meaningful	 to	 domain	 experts.	 Return	 fully	 instantiated	 objects	 or	 collections	 of	 objects	 whose	 attribute	 values	 meet	 the	 criteria,	 thereby	encapsulating	the	actual	storage	and	query	technology,	or	return	proxies	that	give	 the	 illusion	 of	 fully	 instantiated	 aggregates	 in	 a	 lazy	 way.	 Provide	 repositories	 only	 for	 aggregate	 roots	 that	 actually	 need	 direct	 access.	 Keep	 application	 logic	 focused	 on	 the	 model,	delegating	all object	storage	and	access	to	the	repositories.	



### Factories

> NB : only for complex aggregates and value objects ?

Shift	 the	 responsibility	 for	 creating	 instances	 of	 complex	 objects	 and	 aggregates	 to	 a	 separate	 object,	 which	 may	 itself	 have	 no	 responsibility	 in	 the	 domain	 model	 but	 is	 still	 part	of	the	domain	design.	Provide	an	interface	that	encapsulates	all	complex	assembly	and	 that	 does	 not	 require	 the	 client	 to	 reference	 the	 concrete	 classes	 of	 the	 objects	 being	 instantiated.	 Create	 an	 entire	 aggregate	 as	 a	 piece,	 enforcing	 its	 invariants.	 Create	 a	 complex	value	object	as	a	piece,	possibly	after	assembling	the	elements	with	a	builder.	





