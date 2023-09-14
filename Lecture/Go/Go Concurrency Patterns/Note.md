-[YouTube](https://www.youtube.com/watch?v=f6kdp27TYZs)
-[Concurrency Patterns in Go](https://www.youtube.com/watch?v=YEKjSzIwAdA)

## What is a goroutine?
  - It's an independently executing function.

```go

var c chan int
c = make(chan int)

// sending on a channel
c <-1

// receiving from a channel
value := <-c
```

## Synchronization

## The Go approach to concurrency
  - Do not communicate by sharing memory; instead, share memory by communicating.
  - Channels orchestrate; mutexes serialize.

## Go's concurrency toolset
  - go routines
  - channels
  - select
  - sync package

## Where channels fail
  - You can create deadlocks with channels
  - Channels pass around copies, which can impact performance
  - Passing pointers to channels can create race conditions
  - What about `naturally shared` structures like caches or registries?