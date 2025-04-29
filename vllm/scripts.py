# SPDX-License-Identifier: Apache-2.0

from vllm.entrypoints.cli.main import main as vllm_main
from vllm.logger import init_logger
from vllm.entrypoints.openai.cli_args import (make_arg_parser,
                                              validate_parsed_serve_args)

logger = init_logger(__name__)


# Backwards compatibility for the move from vllm.scripts to
# vllm.entrypoints.cli.main
def main():
    logger.warning("vllm.scripts.main() is deprecated. Please re-install "
                   "vllm or use vllm.entrypoints.cli.main.main() instead.")
    vllm_main()
