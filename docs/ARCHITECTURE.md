# Architecture

## Goal

The service is a small HTTP API that records Karma adjustments and returns a person's current daily Karma state. It is a teaching surface, not a production system.

## Starting point

The starter has one FastAPI entry point and a health endpoint. The workshop adds Karma behavior in small changes so each abstraction has a concrete reason.

## Intended boundaries

- **HTTP edge:** FastAPI handlers translate HTTP requests and responses.
- **Karma domain:** the ledger owns adjustment and daily-limit decisions.
- **Storage:** the core path uses in-memory state. SQLite is an optional adapter after the domain has a real persistence seam.

The domain must not import FastAPI or SQLite. A repository port is introduced only when storage needs to vary independently from Karma policy.

## Exclusions

The workshop does not add authentication, authorization, background jobs, Docker Compose, an ORM, migrations, deployment, observability infrastructure, or multi-user concurrency control.
