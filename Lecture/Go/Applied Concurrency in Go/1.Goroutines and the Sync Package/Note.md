## Concurrency vs parallelism

## Goroutines basics
- A goroutine is a function that is capable of running concurrently with other functions.
- To create a goroutine we use the keyword go followed by a function invocation:
```go
go f(x, y, z)
```
- The evaluation of f, x, y, and z happens in the current goroutine and the execution of f happens in the new goroutine.
- Goroutines run in the same address space, so access to shared memory must be synchronized. The sync package provides useful primitives, although you won't need them much in Go as there are other primitives.
- A goroutine is a lightweight thread managed by the Go runtime.

## The syncWaitGroup
- The sync package provides a WaitGroup type for synchronizing concurrent processes.
- A WaitGroup waits for a collection of goroutines to finish.
- The main goroutine calls Add to set the number of goroutines to wait for. Then each of the goroutines runs and calls Done when finished. At the same time, Wait can be used to block until all goroutines have finished.
```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
  defer wg.Done()
  // do something
}()
wg.Wait()
```

## Race conditions
- Race conditions occur when two or more operations must execute in the correct order, but the program has not been written so that this order is guaranteed to be maintained.
- The Go toolchain has a built-in race detector
- Add the -race flag to any go command to enable it.
```bash
go run -race server.go
```

## The sync.Map
- The sync.Map type is a concurrent map with amortized-constant-time loads, stores, and deletes.
- A sync.Map is safe for concurrent use by multiple goroutines without additional locking or coordination.
- Load returns the value stored in the map for a key, or nil if no value is present.
- Store sets the value for a key.
- Delete deletes the value for a key.
- LoadOrStore returns the existing value for the key if present. Otherwise, it stores and returns the given value.
- Range calls f sequentially for each key and value present in the map. If f returns false, range stops the iteration.
```go
var m sync.Map
m.Store("key", "value")
m.Load("key")
m.Delete("key")
m.LoadOrStore("key", "value")
m.Range(func(key, value interface{}) bool {
  // do something
  return true
})
```

## The sync.Mutex
