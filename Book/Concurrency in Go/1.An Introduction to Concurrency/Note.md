# An Introduction to Concurrency
## Moore's Law, Web Scale, and the Mess We're In

## Why Is Concurrency Hard?

## Race Conditions
- A race condition occurs when two or more operations must execute in the correct order, but the program has not been written so that this order is guaranteed to be maintained.
```go
var data int
go func() { data++ }()
time.Sleep(1 * time.Second) // This is bad!
if data == 0 { fmt.Printf("the value is %v.\n", data) }

```

## Atomicity


## Memory Access Synchronization
- call to lock you see can make our program slow
```go
var memoryAccess sync.Mutex
var value int
go func() {
  memoryAccess.Lock()
  value++
  memoryAccess.Unlock()
}()

memoryAccess.Lock()
if value == 0 {
  fmt.Printf("the value is %v.\n", value)
} else {
  fmt.Printf("the value is %v.\n", value)
}

memoryAccess.Unlock()
```

## Deadlocks, Livelocks, and Starvation
- A deadlocked program is one in which all concurrent processes are waiting on one another.
- Livelocks are programs that are actively performing concurrent operations, but these operations do nothing to move the state of the program forward.
- Livelocks are a subset of a larger set of problems called starvation.
- Starvation is any situation where a concurrent process cannot get all the resources it needs to perform work.
- starvation can also apply to CPU, memory, file handles, database connections: any resource that must be shared is a candidate for starvation.


## Determining Concurrency Safety


