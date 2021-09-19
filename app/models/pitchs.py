class Pitch:
  all_pitches = []

  def __init__(self, id, title, pitch, like, dislike):
    self.id = id
    self.title = title
    self.pitch = pitch
    self.like = like
    self.dislike = dislike

    def save_pitch(self):
      Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitch(cls):
      Pitch.all_pitches.clear()
      