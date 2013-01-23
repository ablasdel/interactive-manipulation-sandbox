"""autogenerated by genpy from multi_ros/TopicLinkStats.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TopicLinkStats(genpy.Message):
  _md5sum = "6811ea0daff55386c45f10bd66bfb859"
  _type = "multi_ros/TopicLinkStats"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string topic
uint64 bytes_sent
uint64 bytes_received
"""
  __slots__ = ['topic','bytes_sent','bytes_received']
  _slot_types = ['string','uint64','uint64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       topic,bytes_sent,bytes_received

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TopicLinkStats, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.topic is None:
        self.topic = ''
      if self.bytes_sent is None:
        self.bytes_sent = 0
      if self.bytes_received is None:
        self.bytes_received = 0
    else:
      self.topic = ''
      self.bytes_sent = 0
      self.bytes_received = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2Q.pack(_x.bytes_sent, _x.bytes_received))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic = str[start:end].decode('utf-8')
      else:
        self.topic = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.bytes_sent, _x.bytes_received,) = _struct_2Q.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.topic
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2Q.pack(_x.bytes_sent, _x.bytes_received))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topic = str[start:end].decode('utf-8')
      else:
        self.topic = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.bytes_sent, _x.bytes_received,) = _struct_2Q.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2Q = struct.Struct("<2Q")