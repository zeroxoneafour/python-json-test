# python json-test

WhY iS pYtHoN nOt WoRkInG???

When I invoke `./run.sh`, I get -

```
JSON test - reading file.json
Contents of file.json - {"num-1":1, "str-1":"hello world!", "array-1":[1,"hello again!",23]}

Traceback (most recent call last):
  File "/home/vaughanm/Documents/python/json/json-test.py", line 11, in <module>
    json_object = json.load(json_file)
  File "/usr/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/usr/lib/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.9/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

Why is this?

## license

All code in this project is under the [MIT License](https://mit-license.org), copyright Vaughan Milliman.
