"""**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose
is a bit different. Rather than expose a "text in, text out" API, they expose
an interface where "chat messages" are the inputs and outputs.

**Class hierarchy:**

.. code-block::

    BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501

from langchain.chat_models.anthropic import ChatAnthropic
from langchain.chat_models.azure_openai import AzureChatOpenAI
from langchain.chat_models.bedrock_anthropic import BedrockChatAnthropic
from langchain.chat_models.fake import FakeListChatModel
from langchain.chat_models.google_palm import ChatGooglePalm
from langchain.chat_models.human import HumanInputChatModel
from langchain.chat_models.jinachat import JinaChat
from langchain.chat_models.mlflow_ai_gateway import ChatMLflowAIGateway
from langchain.chat_models.openai import ChatOpenAI
from langchain.chat_models.promptlayer_openai import PromptLayerChatOpenAI
from langchain.chat_models.vertexai import ChatVertexAI

__all__ = [
    "ChatOpenAI",
    "AzureChatOpenAI",
    "BedrockChatAnthropic",
    "FakeListChatModel",
    "PromptLayerChatOpenAI",
    "ChatAnthropic",
    "ChatGooglePalm",
    "ChatMLflowAIGateway",
    "ChatVertexAI",
    "JinaChat",
    "HumanInputChatModel",
]
