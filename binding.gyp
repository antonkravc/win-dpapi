{
  "targets": [
    {
      "target_name": "win-dpapi",
      "sources": [ "src/win-dpapi.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "include"
      ],
      "libraries": [
        "-lcrypt32.lib"
      ]
    }
  ]
}
