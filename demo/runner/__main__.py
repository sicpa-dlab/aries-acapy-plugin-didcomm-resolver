"""Run Universal Resolver DIDComm + Resolver Plugin Demo."""

import json
import time
from typing import Tuple
from . import Agent


def setup() -> Tuple[Agent, dict]:
    """Do agent setup."""
    requester_url = input("Enter the requester URL: ")
    resolver_invite_str = input("Enter the resolver invitation json: ")
    resolver_invite_json = json.loads(resolver_invite_str)

    # Small version compatibility fixes
    resolver_invite_json["handshake_protocols"][
        0
    ] = "https://didcomm.org/didexchange/1.0"
    resolver_invite_json["services"] = resolver_invite_json["service"]
    del resolver_invite_json["service"]

    requester = Agent(requester_url)
    conn = requester.receive_invite(resolver_invite_json)
    time.sleep(1)
    return requester, conn  # type: ignore


def main():
    """Run the demo."""
    requester, connection = setup()

    requester.register_resolver_connection(
        conn_id=connection["connection_id"],
        methods=["github", "ethr", "btcr", "v1", "ion", "key", "elem"],
    )

    print(requester.resolve("did:github:dbluhm"))


if __name__ == "__main__":
    main()
