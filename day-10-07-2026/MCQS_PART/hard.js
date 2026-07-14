export default [
{
id: 101,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "What happens to a module's code context entries located inside the sys.modules tracking table mapping structure if you run import commands repeatedly?",
options: ["The file code recalculates completely from source", "Python pulls the module reference directly out of cache memory without re-execution", "The namespace structures isolate into independent sub-processes", "A compilation warning exception occurs tracking memory bloat"]
},
{
id: 102,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "If a module tracking level configuration defines a restricted global collection named all, what functional visibility behavior is forced during star imports?",
options: ["Only the names matching item strings listed in all are mapped into the local scope", "All names containing double underscores are imported automatically", "The import command fails and raises a global compilation structural warning", "The system namespace marks all internal assets as strictly immutable constants"]
},
{
id: 103,
category: "Variables and Data Types",
difficulty: "hard",
question: "Consider this sequence: listA = [10, [20]]; listB = list(listA). If you run the operational step: listB[1].append(30), what state manifests?",
options: ["listA shifts to [10, [20]], listB shifts to [10, [20, 30]]", "Both listA and listB reflect the updated inner sequence [10, [20, 30]]", "listA shifts to [10, [20, 30]], listB shifts to [10, [20]]", "A shallow mutation validation error blocks execution"]
},
{
id: 104,
category: "Variables and Data Types",
difficulty: "hard",
question: "What core conceptual dynamic defines why a user-defined class object or immutable primitive sequence can act as an acceptable dictionary key?",
options: ["The object implements an immutable layout structure", "The object is hashable, possessing a stable hash code that persists across its lifetime", "The item references are monitored directly by the kernel thread registers", "The instance bypasses normal data verification loops"]
},
{
id: 105,
category: "Strings",
difficulty: "hard",
question: "Given that Python strings are strictly immutable structures, what happens in memory when executing basic string additions inside an extensive concatenation loop?",
options: ["The existing allocation dynamically stretches", "Python continuously instantiates distinct brand-new string allocation objects, increasing memory overhead", "The characters write directly into a local thread stack vector layout", "The string pointer tracking indices switch positions seamlessly"]
},
{
id: 106,
category: "Strings",
difficulty: "hard",
question: "What memory behavior occurs when assigning two independent identical string short literals to separate variables (e.g., s1 = 'hello'; s2 = 'hello')?",
options: ["They point to completely unique memory blocks", "Python applies string interning, optimization structures making both point to the same internal reference", "The system raises a namespace collision warning", "The string trackers convert directly into list arrays"]
},
{
id: 107,
category: "Lists and Tuples",
difficulty: "hard",
question: "What is the outcome of the following slice statement pattern executed against an array list sequence: dataset = [1, 2, 3]; dataset[1:2] = [4, 5, 6]?",
options: ["It produces a multi-dimensional array mapping structure", "The target list grows, structural elements insert replacing the targeted index slice location", "It triggers a standard slicing index error condition", "The collection converts into an immutable tuple object"]
},
{
id: 108,
category: "Lists and Tuples",
difficulty: "hard",
question: "If an immutable tuple data reference contains a nested mutable list tracking item inside its structure, what occurs if you attempt an item append mutation on that list?",
options: ["A TypeError structural exception is thrown immediately", "The nested list mutates successfully, demonstrating that container immutability is not transitive", "The system forces a copy clone optimization step automatically", "The tuple structural wrapper clears its memory allocation tracking"]
},
{
id: 109,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What structural operation anomaly can happen if you introduce a mutable item element, like a list, directly as an evaluated member inside a dictionary tracking key loop?",
options: ["The item converts to a string layout", "It raises a TypeError because mutable collections are unhashable types", "The internal indexing table defaults into an open binary search path", "The structural data maps into an independent storage stack"]
},
{
id: 110,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What is the evaluation behavior when executing an update sequence on nested data layouts via: configA = {'meta': {'id': 1}}; configB = {'meta': {'val': 2}}. What does configA.update(configB) produce?",
options: ["{'meta': {'id': 1, 'val': 2}}", "{'meta': {'val': 2}}", "A nested key validation collision error", "An structural matrix array of parameters"]
},
{
id: 111,
category: "Conditional Statements",
difficulty: "hard",
question: "What logic state manifests from short-circuit tracking when computing the compound evaluation step: outcome = [] or {} or 'Final' or 50?",
options: ["[]", "{}", "'Final'", "50"]
},
{
id: 112,
category: "Conditional Statements",
difficulty: "hard",
question: "Which of the following objects translates as a Truthy entity when checked under boolean validation rules inside conditional structures?",
options: ["0.0", "''", "([0])", "None"]
},
{
id: 113,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "When a Python script file runs directly as the primary execution entry point of a program, what specific value is assigned to its global variable namespace string tag name?",
options: ["'module'", "'main'", "'init'", "'core'"]
},
{
id: 114,
category: "Variables and Data Types",
difficulty: "hard",
question: "If a global tracking parameter is modified inside a local file region scope without using global syntax keywords, what behavioral layout tracking outcome occurs?",
options: ["The global variable updates its tracking attributes", "Python creates a new distinct localized variable block that shadows the global name reference", "The compilation cycle throws a runtime structural collision error", "The data references scale into a locked global state"]
},
{
id: 115,
category: "Strings",
difficulty: "hard",
question: "What structural array output results from performing complex slice sequences across empty range configurations via: 'Data'[:100:2]?",
options: ["'Data'", "An index range processing error", "''", "'Dt'"]
},
{
id: 116,
category: "Lists and Tuples",
difficulty: "hard",
question: "What happens behind the scenes in memory allocations when executing an expansion copy via: matrix = [[0]] * 3; matrix[0][0] = 99?",
options: ["Only the first index item registers the 99 change", "All three list element rows reflect the updated 99 modification because they share identical references", "The operation initiates an allocation segmentation fault", "The system clones independent unique list lines dynamically"]
},
{
id: 117,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "How does the hash uniqueness mechanism inside a set respond if you attempt insertion of objects that evaluate as matching values but have distinct primitive classes (e.g., 1 and 1.0)?",
options: ["Both entries persist as individual elements", "They collide, and the set treats them as identical, retaining only the first encountered element", "The tracking layer maps them across isolated binary nodes", "A structural hash mismatch error triggers a script halt"]
},
{
id: 118,
category: "Conditional Statements",
difficulty: "hard",
question: "What logic value translates from the evaluation sequence: check = (10 > 5) or (1 / 0 == 0)?",
options: ["True", "False", "ZeroDivisionError", "TypeError"]
},
{
id: 119,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "Where does Python look first when matching an item referenced via an import operation before scanning external framework path vectors?",
options: ["The external site-packages folder structures", "The built-in module catalog cache map sys.modules", "The immediate localized system platform runtime path", "The user configuration file system registries"]
},
{
id: 120,
category: "Variables and Data Types",
difficulty: "hard",
question: "What structural mechanism allows custom complex object instances to be safely passed by value reference rather than creating absolute standalone data duplicates?",
options: ["Object references are handled via underlying pointer tracking structures", "The interpreter tracks changes by executing background structural deep clones", "The data fields write directly into protected system static registries", "The fields apply structural string processing checks"]
},
{
id: 121,
category: "Strings",
difficulty: "hard",
question: "What happens if you apply negative step counts on an inverted string slicing operation where boundaries do not align (e.g., 'Python'[2:5:-1])?",
options: ["It returns an inverted substring segment", "It yields an absolute empty string output sequence", "It raises an out-of-bounds indexing error", "It loops characters continuously across the boundary"]
},
{
id: 122,
category: "Lists and Tuples",
difficulty: "hard",
question: "If a slice operation is structured using data boundaries that extend far beyond the actual bounds of a list array, what is the programmatic outcome?",
options: ["The structure triggers an IndexError", "Python limits the execution to the actual available sequence bounds gracefully", "The list pads the empty positions with None tokens", "The operation returns an unallocated memory block pointer"]
},
{
id: 123,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What performance reality manifests regarding dictionary processing speeds if keys generate a massive volume of hash value collision states?",
options: ["The operation instantly raises an internal table crash error", "The time complexity for dictionary lookups degrades from O(1) average toward O(n)", "The system automatically mirrors the values into a tuple tracking tree", "The keys isolate into secondary process tasks"]
},
{
id: 124,
category: "Conditional Statements",
difficulty: "hard",
question: "What structural result is produced from the short-circuit expression logic layout tracking: validation = False and (5 / 0 == 0)?",
options: ["False", "ZeroDivisionError", "True", "None"]
},
{
id: 125,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "What structural behavior occurs if two separate modules execute circular imports (moduleA imports moduleB, and moduleB imports moduleA) at their top-level global scopes?",
options: ["The engine resolves the dependency graph via dynamic threads", "It can trigger an AttributeError or ImportError depending on execution order", "The secondary module file clears its global variable state", "The program converts the modules into localized function structures"]
},
{
id: 126,
category: "Variables and Data Types",
difficulty: "hard",
question: "What built-in system mechanism manages the automatic cleanup of variable references that have dropped to a zero active usage count?",
options: ["Generational tracing sweeps", "Reference counting tracking structures", "Static memory compaction logic", "Namespace allocation audits"]
},
{
id: 127,
category: "Strings",
difficulty: "hard",
question: "What specific text processing outcome is evaluated from executing the code statement: 'test'.join(['1', '2'])?",
options: ["'1test2test'", "'1test2'", "'test1test2'", "TypeError"]
},
{
id: 128,
category: "Lists and Tuples",
difficulty: "hard",
question: "Given lines = [[]] * 2. If you execute lines[0].append(5), followed by lines.append(10), what is the resulting state of lines?",
options: ["[[5], [5], 10]", "[[5], [], 10]", "[[5, 10], [5, 10]]", "[[5], [5]]"]
},
{
id: 129,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What strategy can copy a dictionary containing complex nested properties so modifications to nested structures do not alter the source copy?",
options: ["dict.copy()", "copy.deepcopy()", "dict(target)", "{target}"]
},
{
id: 130,
category: "Conditional Statements",
difficulty: "hard",
question: "What boolean validation truth value status belongs to an active user-defined object instance whose class definition sets bool to return False?",
options: ["It evaluates as Truthy", "It evaluates as Falsy", "It triggers a parsing syntax error", "It forces an internal runtime exception status"]
},
{
id: 131,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "How does the scope resolution behavior locate variable references when a module-level asset is processed within an internal block?",
options: ["It evaluates via the LEGB tracking layout rule lookup order", "It checks class declarations exclusively", "It applies top-down binary graph verification passes", "It accesses thread hardware registers directly"]
},
{
id: 132,
category: "Variables and Data Types",
difficulty: "hard",
question: "What happens when you pass an active mutable list array variable instance as a parameter value to an operation container?",
options: ["The runtime engine creates a local duplicate element segment", "The system transmits a pointer value reference to the original list block allocation", "The system locks the list parameter into a frozen constant layout", "A structural serialization process isolates the data fields"]
},
{
id: 133,
category: "Strings",
difficulty: "hard",
question: "What is the evaluated output generated when a string format operation contains matching indexed variable tags out of sequence order: '{1} {0}'.format('A', 'B')?",
options: ["'A B'", "'B A'", "'A A'", "IndexError"]
},
{
id: 134,
category: "Lists and Tuples",
difficulty: "hard",
question: "What does executing continuous structural comparisons across separate extensive nested lists verify (e.g., [1, [2]] == [1, [2]])?",
options: ["It tracks only base structure locations", "It evaluates matching data values recursively across all nested levels of the collection", "It validates memory locus pointer signatures exclusively", "It returns an internal type validation warning check"]
},
{
id: 135,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What structural tracking behavior is exhibited by the dict.fromkeys([1, 2, 3], []) instantiation layout pattern?",
options: ["Every unique dictionary key tracks a distinct independent empty list structure instance", "All constructed keys point to the exact same shared mutable empty list instance in memory", "The declaration throws an automatic type assignment exception", "The keys map to an immutable placeholder matrix configuration"]
},
{
id: 136,
category: "Conditional Statements",
difficulty: "hard",
question: "What logic valuation rule handles processing multi-part conditions when logical 'and' expressions are chained next to 'or' expressions without explicitly using parentheses?",
options: ["The evaluation tracks strictly from right to left direction", "The operator 'and' takes processing precedence over 'or'", "The operator 'or' takes processing precedence over 'and'", "The operations run completely in a random priority format"]
},
{
id: 137,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "What programmatic outcome occurs if a python script attempts to run a relative import statement pattern while operating as a standalone root execution file?",
options: ["The engine resolves the path using root files", "It throws an ImportError or ValueError indicating parent module tracking failure", "The system converts relative pathways to system absolute pathways", "The module context defaults into an empty tracking dictionary layout"]
},
{
id: 138,
category: "Variables and Data Types",
difficulty: "hard",
question: "What performance optimization occurs when checking value configurations against large collections of items via sets versus lists?",
options: ["Sets use a binary sort pattern taking O(log n) time scales", "Sets evaluate targets via hash table lookups in O(1) average time, regardless of item counts", "Lists implement an optimized index map matching set speeds", "Sets scale their element lookups via active parallel processes"]
},
{
id: 139,
category: "Strings",
difficulty: "hard",
question: "What string text output format is evaluated when running raw string literal escape designators via: len(r'\n')?",
options: ["1", "2", "0", "An invalid string definition error"]
},
{
id: 140,
category: "Lists and Tuples",
difficulty: "hard",
question: "What occurs if you attempt an explicit items value match assignment loop on an empty slice destination target: items = [1, 2]; items[2:] = [3, 4]?",
options: ["The assigned numbers insert at the absolute end position of the target list structure", "The statement throws an out of bounds slice exception", "The values form a separate standalone multi-dimensional layer", "The list array truncates down to an empty collection state"]
},
{
id: 141,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What dictionary structural behavior manifests when using standard view object references (like .keys()) after the underlying source dictionary items grow or shrink?",
options: ["The views retain their original snapshot entries", "The view objects dynamically reflect updates in real time, mirroring the underlying mapping changes", "The program triggers a view isolation collision alert", "The view locks the dictionary from receiving further mutations"]
},
{
id: 142,
category: "Conditional Statements",
difficulty: "hard",
question: "What result is evaluated when tracking relational logical comparisons across string character variables using standard alphabet scales (e.g., 'apple' > 'banana')?",
options: ["True", "False", "TypeError", "SyntaxError"]
},
{
id: 143,
category: "Modules, pip, & Comments",
difficulty: "hard",
question: "What structural processing routine occurs when a directory framework folder contains an entry named init.py?",
options: ["The system flags the pathway as an asset folder space", "The folder structure is recognized and integrated as a loadable Python package entity", "The compiler marks all localized module codes as private files", "The engine restricts module asset sharing pathways across systems"]
},
{
id: 144,
category: "Variables and Data Types",
difficulty: "hard",
question: "What design paradigm describes Python's type evaluation workflow where type safety checks run dynamically at runtime rather than during script compilation loops?",
options: ["Static structural type casting", "Strongly typed dynamic binding", "Weakly typed compilation mapping", "Abstract interface constraint management"]
},
{
id: 145,
category: "Strings",
difficulty: "hard",
question: "What specific text transformation outcome is produced when applying a character slice operation pattern containing missing parameters via: 'Python'[:]?",
options: ["An absolute complete duplicate string sequence reference", "An empty sequence container value", "An evaluation exception loop error state", "The first isolated character string token element"]
},
{
id: 146,
category: "Lists and Tuples",
difficulty: "hard",
question: "What indexing logic reality applies when performing operations on sorted sequences where item elements are evaluated via id checks vs value equality checks?",
options: ["Value equality validates internal contents, while id validates shared memory locus matching", "The tracking parameters map onto identical memory loci locations automatically", "The system rejects performance checks on elements containing tracking values", "The tracking operations operate via parallel vector checks"]
},
{
id: 147,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "Which collection data type provides an unordered structural framework of completely unique components that must all be hashable entities?",
options: ["List", "Set", "Dictionary", "Tuple"]
},
{
id: 148,
category: "Conditional Statements",
difficulty: "hard",
question: "What programmatic outcome occurs when evaluating short-circuit tracking chains containing non-boolean integers (e.g., validation = 0 and 100)?",
options: ["0", "100", "False", "TypeError"]
},
{
id: 149,
category: "Variables and Data Types",
difficulty: "hard",
question: "What design pattern style defines the identity tracking performance check between an active object variable reference and the built-in single instance token placeholder None?",
options: ["variable == None", "variable is None", "variable in None", "not(variable)"]
},
{
id: 150,
category: "Dictionaries and Sets",
difficulty: "hard",
question: "What outcome is produced if a script re-specifies an existing key with a new assignment value inside a dictionary mapping literal declare block?",
options: ["The declaration raises a KeyError", "The subsequent value assignment overwrites the preceding key definition entry", "The key values chain into an ordered sequence tracking list", "The layout processes both keys as distinct map items"]
}
];