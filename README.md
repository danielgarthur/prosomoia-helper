# Prosomoia Helper

A Python library that helps generate prosomoia for [Neanes](https://github.com/danielgarthur/neanes).

## Use case

If the text for the prosomoia are already available in electronic format, then this script can help quickly generate Neanes files for the prosomoia if you already have a Neanes file containing the automela.

## How to use

### Prerequisites

- Python 3.9 or later
- pip

Some familiarity with Python and pip is assumed. The steps below are an example of how one could use the library. See the `examples` folder for more examples.

1. Clone this repository.
2. Run `pip install -r requirements.txt`
3. Create a Neanes file that contains the automela, including the lyrics. Save the file to the root directory of the repo and name it `automela.byz`.
4. Open the file `sample.py` that is found in the root directory of this repository. Copy the text of the prosomoion and paste it into the `text` variable.

   ```python
   import prosomoiahelper

   text = """This is my metered text * that I copied * from the liturgical notes * provided
   by my Archdiocese."""

   overrides = dict()
   overrides['archdiocese'] = 'arch-di-o-cese'
   overrides['copied'] = 'cop-ied'
   overrides['liturgical'] = 'lit-ur-gic-al'

   prosomoiahelper.generate_prosomoia(
       text,
      'automela.byz',
      'prosomoia.byz',
      overrides)
   ```

5. Save the file and run it via `python sample.py`.
6. Open the generated file `prosomoia.byz` in Neanes and check for accuracy.
7. If a word was not hyphenated correctly, add an override. In the above `sample.py`, you can see that we have added overrides for several words, such as `copied`, because the default hyphenation dictionary did not correctly hyphenate it into two syllables.
8. Run the script again after you have added any necessary overrides. Close and re-open the generated file `prosomoia.byz` to check for accuracy.

## More complicated cases

### Ignored Melismas

Sometimes a prosomoia may require a syllable to be placed on a note that has no syllables in the automela. To do this, create a list of element indices for which this applies and pass it as the `ignored_melismas` argument. See the next section for information on how to find the indices.

For example, to treat the 23rd element of the score as a syllable note, use the following.

```python
prosomoiahelper.generate_prosomoia(
    text,
    'automela.byz',
    'prosomoia.byz',
    overrides,
    ignored_melismas=[23])
```

Example 2 in the `examples` folder contains a concrete example.

### Finding element indices

If you read the above, then you are probably wondering how to find the element indices. To do show, pass `print_syllable_index=True` to the `generate_prosomoia` method. This will print out a list of syllables and their assigned element indices. This can help you quickly locate the correct index.

See the example below.

```python
prosomoiahelper.generate_prosomoia(
    text,
    'automela.byz',
    'prosomoia.byz',
    overrides,
    print_syllable_index=True)
```

### Added melismas

Sometimes the automela contains more syllables than are commonly used by the prosomoia. In this case, we want to treat one of the notes with a syllable as a melisma. To do this, create a list of element indices for which this applies and pass it as the `added_melismas` argument.

For example, to treat the 17th element of the score as a melisma, use the following.

```python
prosomoiahelper.generate_prosomoia(
    text,
    'automela.byz',
    'prosomoia.byz',
    overrides,
    added_melismas=[17])
```

Example 2 in the `examples` folder contains a concrete example.
