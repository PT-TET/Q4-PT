# Smuggler

**Advisory**

All the files/scripts here should only be used for authorized testing. Any misuse of this will not be the responsibility of the author or any other collaborator.
***

**References**

Link 1: https://outflank.nl/blog/2018/08/14/html-smuggling-explained/
Link 2: https://blog.talosintelligence.com/html-smugglers-turn-to-svg-images/
***

### How to use

**Required arguments:**

| Argument (short)     | Argument (full)   | Description                               |
| :------------------- |:------------------| :-----------------------------------------|
| -f                   | --file            | The file you would like to embedd.        |
| -n                   | --name            | The name of the file to be downloaded.    |
| -t                   | --type            | Either HTML or SVG.                       |

#### Examples

**HTML:**
```
python3 smuggler.py -f my_file.exe -n output.exe -t html
```

**SVG:**
```
python3 smuggler.py -f my_file.exe -n output.exe -t svg
```

You can optionally set the output HTML/SVG filename with the `-o` or `--output` argument.
