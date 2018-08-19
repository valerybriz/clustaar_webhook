from clustaar.webhook import Webhook, events
from clustaar.schemas.models import StepReachedResponse, ConversationSession, SendTextAction
import conf
from models import Responses


def get_response(incoming_message):
    myResponse = Responses.Responses()
    incoming_text = incoming_message.get("data").get("step").get("actions")[0].get("alternatives")
    result = myResponse.find_response_by_action(incoming_text[0], incoming_message.get("botID"))
    if result != "error":
        return result.get("outtext")
    else:
        return ""


def handler(request, response, notification):
    my_action = get_response(request.json)

    actions_to_returns = [
        SendTextAction(alternatives=[my_action])
    ]

    return StepReachedResponse(actions=actions_to_returns)


app = Webhook(auth_username=conf.BOT_AUTH_USERNAME, auth_password=conf.BOT_AUTH_PASS)
app.on(events.CONVERSATION_STEP_REACHED, handler)
