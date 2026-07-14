export default [
  {
    id: 51,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What statement format imports a specific asset named 'calculate' from a module named 'math_utils' under the custom local alias name 'calc'?",
    options: ["import calculate as calc from math_utils", "from math_utils import calculate as calc", "import math_utils.calculate as calc", "from math_utils import calc as calculate"]
  },
  {
    id: 52,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What happens inside a script namespace if you run the direct instruction: from logging import *?",
    options: ["It imports only public variables matching string tags", "It imports all names without trailing underscores into the current local namespace", "It creates an internal nested module reference named logging", "It triggers a runtime namespace validation exception"]
  },
  {
    id: 53,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "Which of the given object configurations is a distinct example of an immutable data structure asset type?",
    options: ["List", "Dictionary", "Tuple", "Set"]
  },
  {
    id: 54,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What identity mapping operator evaluates to True if two separate distinct variables point precisely to the exact same memory locus?",
    options: ["==", "is", "in", "id"]
  },
  {
    id: 55,
    category: "Strings",
    difficulty: "medium",
    question: "What is the character slice output evaluated from the execution of: 'Framework'[1:6:2]?",
    options: ["'rme'", "'rmw'", "'rwk'", "'faw'"]
  },
  {
    id: 56,
    category: "Strings",
    difficulty: "medium",
    question: "Which string operation separates an inline sentence string structure into an ordered list sequence of words using empty space boundaries?",
    options: ["split()", "join()", "strip()", "partition()"]
  },
  {
    id: 57,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What slice structure will securely generate an inverted mirror copy of an entire list array instance?",
    options: ["list[::-1]", "list[1:-1]", "list[-1:1]", "list.reverse()"]
  },
  {
    id: 58,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What is the structural outcome of the following unpack operation sequence: a, *b, c = [1, 2, 3, 4, 5]?",
    options: ["a=1, b=2, c=3", "a=1, b=[2, 3, 4], c=5", "a=1, b=[2, 3], c=[4, 5]", "SyntaxError"]
  },
  {
    id: 59,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which method fetches a dictionary value corresponding to a key, returning a fallback default value instead of throwing a KeyError if the key is absent?",
    options: ["pop()", "fetch()", "get()", "lookup()"]
  },
  {
    id: 60,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "What set configuration method tracks items present in either setA or setB, but completely excludes elements intersecting both?",
    options: ["difference()", "symmetric_difference()", "intersection()", "union()"]
  },
  {
    id: 61,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What is the valid syntax structure for a single-line conditional ternary operation assignment layout?",
    options: ["value = condition ? x : y", "value = x if condition else y", "value = if condition then x else y", "value = condition(x, y)"]
  },
  {
    id: 62,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What is the structural evaluation outcome when processing the following chained range expression condition: 5 < 10 > 2?",
    options: ["True", "False", "TypeError", "SyntaxError"]
  },
  {
    id: 63,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What file naming strategy maps out the explicit targeted versions of all packages needed to replicate an environment through pip?",
    options: ["setup.py", "requirements.txt", "packages.json", "pip.conf"]
  },
  {
    id: 64,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What tracking method function can be used to isolate the integer address signature identifier of an active variable reference context?",
    options: ["id()", "address()", "hex()", "loc()"]
  },
  {
    id: 65,
    category: "Strings",
    difficulty: "medium",
    question: "What sequence cleanup result is produced when calling the string method execution: '   Data   '.strip()?",
    options: ["'   Data'", "'Data   '", "'Data'", "'Da ta'"]
  },
  {
    id: 66,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What slice definition reads a subset of items from index 2 up to, but strictly excluding, index 7 from list records?",
    options: ["records[2:7]", "records[2:6]", "records[3:7]", "records[2::7]"]
  },
  {
    id: 67,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which statement configuration merges the keys and values of dictionary sourceB directly into dictionary targetA?",
    options: ["targetA.append(sourceB)", "targetA.update(sourceB)", "targetA.extend(sourceB)", "targetA.add(sourceB)"]
  },
  {
    id: 68,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "Which of the following evaluation patterns tests if a specific item object does NOT reside inside a targeted container structure?",
    options: ["item not in container", "not(item in container)", "item != container", "item is not in container"]
  },
  {
    id: 69,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "If a module file named engine.py is loaded via an import step, what implicit property variable tracks the name string of that module?",
    options: ["engine.__name__", "engine.__file__", "engine.__id__", "engine.__package__"]
  },
  {
    id: 70,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What category of data type allows internal structural updates without modifying its primary base memory allocation lookup reference?",
    options: ["Immutable type", "Mutable type", "Static type", "Constant type"]
  },
  {
    id: 71,
    category: "Strings",
    difficulty: "medium",
    question: "Which method handles replacing occurrences of a target phrase segment inside an unchangeable base string framework?",
    options: ["update()", "replace()", "modify()", "switch()"]
  },
  {
    id: 72,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What index modification occurs when you execute structural tuple packing via coordinates = 10, 20, 30?",
    options: ["It transforms into an ordered list", "It packs integers into a tuple structure", "It produces a dictionary set", "It raises a assignment error"]
  },
  {
    id: 73,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which method drops a specific item out of a dictionary mapping by its key designator and passes back the extracted value asset?",
    options: ["remove()", "discard()", "pop()", "delete()"]
  },
  {
    id: 74,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What logical operator exhibits short-circuiting logic by instantly returning False if the first condition check evaluates to False?",
    options: ["or", "not", "and", "xor"]
  },
  {
    id: 75,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What terminal prompt syntax executes the automated upgrade sequence for a pip package named tools?",
    options: ["pip update tools", "pip install --upgrade tools", "pip upgrade tools", "pip renew tools"]
  },
  {
    id: 76,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What boolean output sequence results from running the matching comparison: 10 == 10.0?",
    options: ["True", "False", "TypeError", "RuntimeError"]
  },
  {
    id: 77,
    category: "Strings",
    difficulty: "medium",
    question: "What formatting tool strategy links array tokens into a clean unified string string based on a joining token pattern?",
    options: ["split()", "join()", "combine()", "attach()"]
  },
  {
    id: 78,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What list process appends each item of an external iteration sequence individually into the targeted base list?",
    options: ["append()", "extend()", "insert()", "merge()"]
  },
  {
    id: 79,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which set method checks if all components of a target set container exist completely within an external collection instance?",
    options: ["issubset()", "issuper()", "isdisjoint()", "intersection()"]
  },
  {
    id: 80,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What logic design handles testing nested conditions across independent structural level checks sequentially?",
    options: ["Chained conditions", "Ternary trees", "Switch configurations", "Parallel matrices"]
  },
  {
    id: 81,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What layout configuration occurs if an imported module includes sub-elements that are referenced via package directory notation?",
    options: ["Dot notation formatting", "Hyphen binding setup", "Slash path navigation", "Arrow indicator tags"]
  },
  {
    id: 82,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What identity calculation tracks whether two distinct variable tracking handles do NOT map to the same memory reference location?",
    options: ["is not", "!=", "not in", "is reverse"]
  },
  {
    id: 83,
    category: "Strings",
    difficulty: "medium",
    question: "Which method formats numeric alignment layout inside a string sequence by prepending padding zeros up to a target size width?",
    options: ["rjust()", "zfill()", "pad()", "center()"]
  },
  {
    id: 84,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What list index lookup operation finds the position of the first occurrence of an item inside list grids?",
    options: ["find()", "index()", "locate()", "position()"]
  },
  {
    id: 85,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "What structure format generates a nested view of matching key-value pairs from an active dictionary mapping structure?",
    options: ["keys()", "values()", "items()", "entries()"]
  },
  {
    id: 86,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What is the evaluated result of the following conditional code tracking logic: active = [] if [] else [1]?",
    options: ["[]", "[1]", "False", "None"]
  },
  {
    id: 87,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "Which system directive tracks the list architecture of system directory search paths utilized by module import processes?",
    options: ["sys.path", "sys.locations", "os.path", "sys.modules"]
  },
  {
    id: 88,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "What type of data category transformation occurs when combining an integer element alongside a float object inside an operation expression?",
    options: ["Explicit type casting", "Implicit type conversion", "Type definition error", "Dynamic string translation"]
  },
  {
    id: 89,
    category: "Strings",
    difficulty: "medium",
    question: "What slice return result is generated when calling: 'Database'[-4:]?",
    options: ["'Data'", "'base'", "'abas'", "'ebas'"]
  },
  {
    id: 90,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What method reverses the physical storage ordering of a mutable list framework in-place without generating a secondary copy structure?",
    options: ["reverse()", "inverted()", "flip()", "sort(reverse=True)"]
  },
  {
    id: 91,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which set deletion method discards an active element component from a set structure but completely avoids a KeyError if that target element doesn't exist?",
    options: ["remove()", "discard()", "pop()", "clear()"]
  },
  {
    id: 92,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What boolean status yields from evaluating the chained relational logic expression: 15 > 10 == 10?",
    options: ["True", "False", "TypeError", "SyntaxError"]
  },
  {
    id: 93,
    category: "Modules, pip, & Comments",
    difficulty: "medium",
    question: "What specific environment inventory format uses pip freeze to map active operational modules into target installation files?",
    options: ["requirements file distribution", "setup distribution package", "manifest inventory config", "metadata configuration bundle"]
  },
  {
    id: 94,
    category: "Variables and Data Types",
    difficulty: "medium",
    question: "Which of the following data structures is categorized as an unchangeable, immutable sequence type allocation?",
    options: ["frozenset", "dict", "list", "bytearray"]
  },
  {
    id: 95,
    category: "Strings",
    difficulty: "medium",
    question: "Which validation check determines if a string text configuration is structured with only alphanumeric symbols present?",
    options: ["isalpha()", "isalnum()", "isnumeric()", "isascii()"]
  },
  {
    id: 96,
    category: "Lists and Tuples",
    difficulty: "medium",
    question: "What structural operation sequence allows separating items out of a packed tuple structure across independent localized tracking variables?",
    options: ["Tuple slicing", "Tuple unpacking", "Tuple composition", "Tuple parsing"]
  },
  {
    id: 97,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "What method is used to return a view of all values present inside a dictionary?",
    options: ["keys()", "values()", "items()", "all()"]
  },
  {
    id: 98,
    category: "Conditional Statements",
    difficulty: "medium",
    question: "What tracking behavior is shown when the first term of an 'or' logic processing loop is evaluated as True?",
    options: ["It tests the second term", "It short-circuits and skips evaluating the rest", "It raises a structural processing error", "It sets the whole system state to null"]
  },
  {
    id: 99,
    category: "Dictionaries and Sets",
    difficulty: "medium",
    question: "Which set operation yields a new set containing elements that are common to both starting sets?",
    options: ["union()", "intersection()", "difference()", "symmetric_difference()"]
  },
  {
    id: 100,
    category: "Strings",
    difficulty: "medium",
    question: "What string method strips away whitespace characters exclusively from the trailing right side of a string?",
    options: ["strip()", "lstrip()", "rstrip()", "cut()"]
  }
];