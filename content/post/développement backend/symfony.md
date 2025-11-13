# Messenger



## **[Symfony Event Dispatcher](https://symfony.com/doc/current/components/event_dispatcher.html)** vs Domain events

- Events are mutable in symfony
- plus the symfony component relies on strings as event names (but we can use class constants)
- and string as method names (but also closures)
- NB : The wiring is done in a compiler pass which does not belong to the domain .. ?
- See [difference between messenger and event dispatcher](https://symfonycasts.com/screencast/messenger/dispatch-event)

  - Messenger allows your handlers to be called *asynchronously*, whereas listeners to events from the EventDispatcher are *always* synchronous.
  - [EventDispatcher communicates back](https://symfonycasts.com/screencast/messenger/messenger-event-dispatcher#eventdispatcher-communicates-back)
  - if you simply want to say "this thing happened" and you don't need any feedback from possible listeners or handlers, use Messenger.
  - NB : So for domain events we could actually use messenger ..!

## [Difference between a command bus and an event bus](https://symfonycasts.com/screencast/messenger/other-middleware#play)

- each command should have exactly one handler: we're *commanding* that something perform a specific action
- But an event is something that's usually dispatched *after* that action is taken, and the purpose is to allow anyone else to take any *secondary* action - to *react* to the action.
- See [symfony's multiple bus example implementing CQRS](https://symfony.com/doc/current/messenger/multiple_buses.html)
- The command bus would use a validation NB : not necessary, validation can be done before event generation) and transaction middleware (don't need to call flush in the handler ! also not necessary if transactions are handled elsewhere)
- The event bus would have `default_middleware: allow_no_handlers`
- Plus we can disable autowiring and tag handlers [to work only with a specific bus](https://symfonycasts.com/screencast/messenger/bus-organization#play)
- The query bus pattern is fine but is not typed in symfony

## [Priority](https://symfonycasts.com/screencast/messenger/message-subscriber#play)

- Transport priority : eg async / async_priority_high : changes the order in which messages are handled 
- Handler priority : only useful when setting multiple handlers. The priority doesn't change the order in which messages are handled, only the handlers for each message