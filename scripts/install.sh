#!/usr/bin/env bash
# Install the Flux Cursor skill by symlinking this repo into ~/.cursor/skills/flux
set -euo pipefail

REPO_PATH="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="${HOME}/.cursor/skills"
TARGET="${SKILLS_DIR}/flux"

mkdir -p "${SKILLS_DIR}"

if [ -e "${TARGET}" ] || [ -L "${TARGET}" ]; then
  if [ -L "${TARGET}" ]; then
    rm "${TARGET}"
  else
    echo "Path already exists and is not a symlink: ${TARGET}" >&2
    exit 1
  fi
fi

ln -s "${REPO_PATH}" "${TARGET}"
echo "Linked ${TARGET} -> ${REPO_PATH}"
echo "In Cursor chat, mention Flux or ask the agent to use the flux skill."
