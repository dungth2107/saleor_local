from ..core.notifications import get_site_context
from ..core.notify_events import NotifyEventType


def send_gift_card_notification(user, app, email, gift_card, manager):
    """Trigger sending a gift card notification for the given recipient."""
    payload = {
        "requester": {
            "user_id": user.id if user else None,
            "email": user.email if user else None,
            "app_id": app.id if app else None,
            "app_name": app.name if app else None,
        },
        "recipient_email": email,
        "gift_card": {"id": gift_card.id, "code": gift_card.code},
        **get_site_context(),
    }
    manager.notify(NotifyEventType.SEND_GIFT_CARD, payload=payload)