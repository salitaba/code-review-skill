---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
runs: 1
---

Review this change as you would review a pull request.

There is no repository to search. The files below are the complete relevant
context.

**Changed — `.github/workflows/release.yml`:**

```diff
 name: release
 on:
   release:
     types: [published]
 
-permissions:
-  contents: read
+permissions: write-all
 
 jobs:
   build:
     runs-on: ubuntu-latest
+    timeout-minutes: 20
     steps:
       - uses: actions/checkout@v4
       - run: ./gradlew build
 
-      - name: Upload artifact
-        uses: actions/upload-artifact@v4
-        with:
-          name: app
-          path: build/libs/*.jar
-
+      - name: Announce release
+        run: |
+          echo "Releasing: ${{ github.event.release.name }}"
+          ./scripts/announce.sh "${{ github.event.release.body }}"
+
       - name: Publish
-        uses: acme/publish-action@v1
+        uses: acme/publish-action@v1
         with:
           token: ${{ secrets.PUBLISH_TOKEN }}
```

**Unchanged — `.github/workflows/publish-artifacts.yml`** (shown for context):

```yaml
 name: publish-artifacts
 on:
   workflow_run:
     workflows: [release]
     types: [completed]
 permissions:
   contents: read
 jobs:
   upload:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/download-artifact@v4
         with:
           name: app
       - uses: actions/upload-release-asset@v1
```

Report findings using your normal review output and severity scale.
