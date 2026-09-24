
from abc import ABC, abstractmethod


class Video(ABC): #abstract base clas: defines rules for their subclasses
    """
    Subject interface. Both the real video and its proxy expose this.
    """

    @abstractmethod    #en este caso obliga a sus subclases a implementar el metodo play
    def play(self) -> str:
        raise NotImplementedError


class RealVideo(Video):
    """
    The expensive resource: loading a video "file" is slow and should only
    happen once, and only when the video is actually about to be played.
    """

    load_count = 0

    def __init__(self, title: str, video_path: str):
        self.title = title
        self.video_path = video_path
        self._load_from_disk() #cuando haces video= real video se ejecuta esto que lo desarga

    def _load_from_disk(self) -> None:
        RealVideo.load_count += 1

    def play(self) -> str:
        return f"Playing '{self.title}' from {self.video_path}"


class ProxyVideo(Video):
    """
    Virtual proxy: stands in for a RealVideo without loading it until the
    first `play()` call, then reuses the same RealVideo for later calls.
    """

    def __init__(self, title: str, video_path: str):
      # TODO: store title/video_path, and keep a reference to the (not yet
      # created) RealVideo, e.g. self._real_video = None
      self.title = title
      self.video_path = video_path
      self._real_video = None   #aqui no estamos descargando el video eso llega luego cuando se hace el play

    def play(self) -> str: #aqui, cuando se ejecuta el play ya se descarga
      # TODO: create the RealVideo lazily on first play() and cache it,
      # then delegate to it on this and every subsequent call.
      if self._real_video is None:
          self._real_video = RealVideo(self.title, self.video_path)
      return self._real_video.play() #y delega en el real video
