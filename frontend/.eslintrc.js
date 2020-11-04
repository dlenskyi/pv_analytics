module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },
  env: {
    node: true,
    browser: true,
  },
  plugins: [
    'vue'
  ],
  extends: [
    'plugin:vue/essential',
    'eslint:recommended'
  ],
  rules: {
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    "indent": ["error", 2],
    'semi': ["error", 'never'],
    'no-tabs': 0,
    'vue/script-indent': [
      'error',
      2,
      {
        'baseIndent': 1,
        'switchCase': 1
      }
    ],
    "vue/html-indent": ["error", 2, {
      "attribute": 1,
      "baseIndent": 1,
      "closeBracket": 0,
      "alignAttributesVertically": true,
      "ignores": []
    }],
    'no-console': 1,
  },
  overrides: [
    {
      "files": ["*.vue"],
      "rules": {
        "indent": "off"
      }
    }
  ],
}
