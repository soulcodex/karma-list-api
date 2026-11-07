# Architecture

## Goal

The workshop target is a small HTTP API that records Karma adjustments and returns a person's
current daily Karma state. It is a teaching surface, not a production system.

## Workshop baseline

The checked-in baseline has only a FastAPI `GET /health` endpoint and its focused test. The endpoints,
domain model, storage choice, and policy below are attendee work guided by the target contract.

## Intended boundaries

- **HTTP edge:** FastAPI handlers translate HTTP requests and responses.
- **Karma domain:** typed concepts and the ledger own Karma state and daily-budget policy.
- **Storage:** in-memory state is sufficient for the core path. SQLite is an optional adapter after
  the domain has a real persistence seam.

The domain must not import FastAPI or SQLite. A repository port is introduced only when storage
needs to vary independently from Karma policy.

## Exclusions

The workshop does not add authentication, authorization, background jobs, Docker Compose, an ORM,
migrations, deployment, observability infrastructure, or multi-user concurrency control.
