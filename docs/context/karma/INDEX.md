# Karma module context

## Goal

Record positive and negative Karma for a person, then expose that person's recorded adjustments and
current daily balance through a small HTTP API.

## Vocabulary

- **Person:** the recipient of a Karma adjustment. The first version identifies a person by a
  non-empty name.
- **Adjustment:** one non-zero integer number of Karma points assigned to a person.
- **Daily balance:** the sum of that person's adjustments for one UTC calendar day.

## Invariants

1. An adjustment cannot be zero.
2. For one person and one UTC calendar day, positive adjustments cannot sum to more than `+5`.
3. For one person and one UTC calendar day, negative adjustments cannot sum to less than `-5`.
4. A rejected adjustment does not change the recorded list or either daily total.
5. The same limits apply regardless of whether points are added in one adjustment or several.

The positive and negative limits are independent. A person can have both positive and negative
adjustments on the same day if each directional total stays within its limit.

## HTTP contract

### `POST /karma`

Records one adjustment.

Request body:

```json
{
  "person": "Ada",
  "points": 1
}
```

The service returns a successful response for an accepted adjustment. A request that violates a
Karma invariant returns a clear client error and leaves state unchanged.

### `GET /karma/{person}`

Returns the named person's recorded adjustments and current UTC-day balance. The exact response
shape is decided when the first endpoint test introduces it.

## Storage and time

The core workshop path uses in-memory storage. It is expected to reset on restart. SQLite is an
optional local adapter and requires no container, server, or ORM.

All daily limits use UTC dates. Time is treated as a dependency when tests need to control the day
boundary.

## Non-goals

- Authentication and authorization
- Reputation ranking or a global leaderboard
- Editing or deleting adjustments
- Cross-day aggregation
- Concurrent write handling
- Production persistence, migrations, backups, or deployment
