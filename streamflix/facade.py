
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade: #simplificamos para el cliente (solo hace subscribe y watch) no tiene que preocuparse de los detalles de los pagos ni de los videos
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor): #imp recibe payment processor (le vale cualquier metodo de pago)
      # TODO: store the payment processor and start unsubscribed
      self._subscribed = False #(cuando init el usuario no esta subscrito)
      self.payment_processor = payment_processor # se guarda el metodo de pago que nos pasan

    def subscribe(self, monthly_fee: float) -> str:
      # TODO: charge `monthly_fee` through the payment processor, mark the
      # account as subscribed, and return the processor's receipt string.
      receipt = self.payment_processor.pay(monthly_fee)
      self._subscribed = True
      return receipt

    def watch(self, video: Video) -> str:
      # TODO: if not subscribed, raise PermissionError("subscription required").
      # Otherwise delegate to `video.play()` and return its result.
      if not self._subscribed:
          raise PermissionError("subscription required")
      return video.play()
      
