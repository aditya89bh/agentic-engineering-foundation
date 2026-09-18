# Day 6 Failure Cases

## Same memory stored repeatedly
**Risk:** duplicate evidence appears stronger than it is.

## Stale price reused
**Risk:** an old value is treated as current truth.

## Rejected supplier recommended again
**Risk:** relevant decision memory was not retrieved.

## Low-confidence inference treated as fact
**Risk:** speculative model output becomes durable truth.

## Unrelated memory retrieved
**Risk:** memory pollutes context and changes the decision.

## Memory missing source
**Risk:** the system cannot evaluate trust or provenance.

## Corrupt memory record
**Risk:** malformed records break retrieval or downstream context assembly.

## Conflicting memories
**Risk:** two incompatible facts are returned with no precedence policy.

## Deleted supplier still retrieved
**Risk:** obsolete entities remain active in memory.

## Memory store unavailable
**Risk:** the agent silently behaves as if no history exists.

## Debugging question

> Did the model reason badly, or did the memory system store or retrieve the wrong thing?
