# Architecture

## Goal

The service is a small HTTP API that records Karma adjustments and returns a person's current daily
Karma state. It is a teaching surface, not a production system.

## Workshop baseline

The baseline has a FastAPI edge, typed Karma concepts, an in-memory ledger, and happy-path HTTP
tests. It accepts non-zero adjustments and returns a person's current UTC-day state. It deliberately
does not enforce the daily directional budgets.

## Intended boundaries

- **HTTP edge:** FastAPI handlers translate HTTP requests and responses.
- **Karma domain:** typed concepts and the ledger own Karma state. The daily-budget policy is the
  workshop change.
- **Storage:** the core path uses in-memory state. SQLite is an optional adapter after the domain
  has a real persistence seam.

The domain must not import FastAPI or SQLite. A repository port is introduced only when storage
needs to vary independently from Karma policy.

## Exclusions

The workshop does not add authentication, authorization, background jobs, Docker Compose, an ORM,
migrations, deployment, observability infrastructure, or multi-user concurrency control.
