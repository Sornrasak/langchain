from abc import ABC
from typing import Any, AsyncIterator, Iterator, List, Optional

from libs.langchain.langchain.callbacks.manager import CallbackManagerForLLMRun
from libs.langchain.langchain.schema.output import ChatGenerationChunk

from langchain.callbacks.manager import AsyncCallbackManagerForLLMRun
from langchain.chat_models.base import BaseChatModel
from langchain.llms.bedrock import BedrockBase
from langchain.schema.messages import BaseMessage
from langchain.schema.output import ChatResult


class BaseBedrockChat(BaseChatModel, BedrockBase, ABC):
    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        raise NotImplementedError(
            """Bedrock doesn't support stream requests at the moment."""
        )

    def _astream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[ChatGenerationChunk]:
        raise NotImplementedError(
            """Bedrock doesn't support async requests at the moment."""
        )

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        raise NotImplementedError(
            """Bedrock doesn't support async strem requests at the moment."""
        )
