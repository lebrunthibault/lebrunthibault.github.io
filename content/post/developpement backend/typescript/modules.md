# Types of modules

Node.js has two module systems: [CommonJS](https://nodejs.org/api/modules.html) modules and ECMAScript modules.

Commonjs: `require()`

Es modules: `import from`

## Configuration

- via a file extension : .cjs for CommonJs, .mjs for ES modules
- package.json "type": "commonjs" for CommonJs or "module" for ES modules





[The different js module formats](https://code-trotter.com/web/understand-the-different-javascript-modules-formats/)

# CommonJS

- Uses require() and exports.
- `module.exports` is specific to Node.js

![image-20220403180303986](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220403180303986.png)

- The commonJS team created this API as a **synchronous** one which is not that good for browsers... Moreover, **Commonjs isn't natively understood by browsers**; it requires either a loader library or some transpiling

# Asynchronous Module Definition (AMD)

- AMD is some kind of a split of CommonJS. It has been created by members of the CJS team that disagreed with the direction taken by the rest of the team.
- They've decided to create AMD to support **asynchronous** module loading. This is the module system used by [RequireJS](https://requirejs.org/) and that is working client-side (in browsers).

![image-20220403180526230](https://raw.githubusercontent.com/lebrunthibault/images_bucket/master/img/image-20220403180526230.png)

- This example works only if you have requirejs on your website. You can find some other [AMD examples](https://clubmate.fi/requirejs-from-scratch-and-the-amd-module-patterns/).




# Universal Module Definition (UMD)

- It is based on AMD but with some special cases included to handle CommonJS compatibility.
- Unfortunately, this compatibility adds some complexity that makes it complicated to read / write

# ES2015 Modules (ESM)

- new standard from ecmascript with advandates :
  - easy to read
  - easy to analyze for bundlers (e.g. tree-shaking : remove unused code)
  - not yet asynchronous modules
  - not implemented everywhere so needs transpiling