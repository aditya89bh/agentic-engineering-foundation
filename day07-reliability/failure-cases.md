# Day 7 Failure Cases

## Infinite retry loop
**Risk:** recovery logic becomes a runaway process.

## Retrying invalid input
**Risk:** permanent failures waste time and cost.

## Fallback also fails
**Risk:** the system needs a terminal policy such as NEEDS_HUMAN.

## Circuit remains open forever
**Risk:** the dependency can never re-enter service.

## Timeout missing
**Risk:** one blocked dependency can stall the entire task.

## Duplicate side effect after retry
**Risk:** a repeated action creates duplicate orders, messages, or writes.

## Failure swallowed silently
**Risk:** the system appears healthy while losing work.

## Partial success reported as full success
**Risk:** users receive stronger confidence than the evidence supports.

## Retry budget ignored
**Risk:** local recovery violates the global task budget.

## Wrong error classification
**Risk:** the system retries what should fail, or fails what could recover.

## Model loops after a tool failure
**Risk:** the decision policy repeats the same unsuccessful behavior.

## Debugging question

> Is the agent recovering safely, or merely trying again?
