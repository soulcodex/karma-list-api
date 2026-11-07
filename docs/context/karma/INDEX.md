# Karma module context

## Goal

Record positive and negative Karma for a person, then expose that person's recorded adjustments and
current daily balance through a small HTTP API.

This is the workshop's supplied product contract. It leaves implementation choices open so attendees
can use their harness to make and verify them.

## Vocabulary

- **Person ID:** an opaque UUID that identifies the recipient of a Karma adjustment. It is an
  identifier, not a display name or an assertion about identity.
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

## Workshop baseline and target

The supplied baseline exposes only `GET /health`. Attendees build the Karma endpoints, typed
concepts, storage, and daily-budget policy from this contract. Keep the policy outside the FastAPI
handlers. The HTTP edge translates requests and responses only.

## HTTP contract

### `POST /karma`

Records one adjustment.

Request body:

```json
{
  "person_id": "66e4e8b7-c91b-4cb4-a453-772560a792a7",
  "points": 1
}
```

An accepted adjustment returns `201`:

```json
{
  "person_id": "66e4e8b7-c91b-4cb4-a453-772560a792a7",
  "points": 1
}
```

A request that would exceed either daily directional limit returns `409` with this response and
leaves state unchanged:

```json
{
  "detail": "daily Karma limit exceeded"
}
```

### `GET /karma/{person_id}`

Returns the identified person's recorded adjustments and current UTC-day balance:

```json
{
  "person_id": "66e4e8b7-c91b-4cb4-a453-772560a792a7",
  "adjustments": [1, -1],
  "daily_balance": 0
}
```

An unknown person ID returns the same shape with an empty `adjustments` list and `daily_balance` of
`0`.

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
