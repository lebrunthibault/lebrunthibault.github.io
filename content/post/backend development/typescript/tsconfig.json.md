# Options

**target**: target [version of ecmascript](https://formationjavascript.com/versions-de-javascript-histoire-et-futur/) for compiling. ES6 (2015) is a good choice, es2020 for personal projects

**esModuleInterop**: 

- Problem occurs when we want to import CommonJS module into ES6 module codebase
- ES6 module spec only allows default requiring object, not functions 

**moduleResolution**: "node" or "node12" / "nodenext". "classic" is phased out

**isolatedModules**: necessary for vite. Warns when using language constructs (e.g. namespace) not compatible with single-file transpilation process.

**strict**: The `strict` flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness
