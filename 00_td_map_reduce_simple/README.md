```bash
# Test mapper.py and reducer.py locally first

# very basic test
echo "si les chaussettes sont sèches ou si les chaussettes ne sont pas sèches" | python ./mapper.py | sort | python ./reducer.py
```

Source (base code, slightly refactored): https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/