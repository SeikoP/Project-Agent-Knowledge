# Storybook Expressive Chibi — Production Design System

Status: approved art-direction foundation; production system specification v1
Art direction ID: storybook-expressive-chibi
Art direction version: 1
Canonical demo: C1 in this document's references directory
Canvas target: portrait 1080 × 1920 (9:16)

This document is the single visual source of truth for production video assets. Runtime Writer Context and its allowed_assets list remain the authority for which concrete assets a StoryGraph may select. This specification defines how approved production assets are made and described; it does not itself add demo references to the runtime catalog.

## 1. Direction and references

Storybook Expressive Chibi combines the scene depth, mature proportions, warm palette, and prop treatment of C1's Storybook base with slightly clearer eye, brow, and mouth acting. Characters remain storybook illustrators' characters: not stickers, mascots, fashion dolls, or children's cartoons.

C1 is the approved foundation, not a freeze of every SVG. The character masters, expression references, and camera plates under references/storybook-expressive-chibi-v1/C1/ are visual evidence for this system. They may be refined when production-quality masters are made, provided they follow these rules. They are demo compositions, not production assets and must never enter allowed_assets.

A2 and B2 are historical exploration only. Do not import their distinctive eye scale, silhouette, color or rendering choices into production. Old chibi-object-theater and chibi-human-story assets are legacy directions; neither is the source for new assets. Functional pack tags do not define art direction.

Use the machine-readable tokens in tokens.storybook-expressive-chibi.v1.json for numeric color and line values. If a value conflicts with this prose, the token file controls measurable drawing values and this document controls design intent.

## 2. Visual tokens and construction

### Canvas and drawing units
- Compose for 1080 × 1920 portrait. C1 demo source plates use viewBox 0 0 720 1280 and scale 1.5 to target. Production files may use another internal viewBox when their export is deterministic.
- Keep art optically centered inside the shot-specific composition, not automatically centered in the canvas.
- Core palette: ink #594651; warm wall #E9D9BD and #D9C3A4; window #9DB8AE; sage #C3D2B3; table #A66E52; soft shadow #8A685B; paper #F5EAD3; cream highlight #FFFDF2.
- Skin is warm and varied per identity. Hair and clothing carry secondary identity colors; do not use color as the only identity signal.
- C1 outline is rounded and warm dark ink, not pure black. On the 720 × 1280 reference grid, outer character outline is 4.5 units; eye outline 4; eyebrow 4.2; face/nose/mouth internal marks roughly 3.4–3.8. Prefer round caps and joins.
- Use broad, quiet shading with one clear light direction. Skin shading may move from warm cream #FFF0D8 toward muted rose #C87970 at low opacity. Paper grain, when used, is sparse and subtle (roughly 0.12–0.17 opacity at source). Do not use grain to hide poor vector construction.
- Highlights use warm cream. Shadows stay warm and low contrast. Avoid hard black shadows, glossy plastic shine, gradients on every object, and noisy texture.

### Character proportions
Measure against the supplied C1 identity references. The following ranges are construction targets, not independent style variants:
- Head height is about 42–48% of the standing figure's visible height. Keep C1's mature small-body / large-head balance; do not push toward A2's oversized head.
- Torso from shoulder to hip is about 0.9–1.1 head heights. Legs from hip to sole are about 1.0–1.25 head heights. Arms are short and rounded, reaching around hip to upper thigh at rest.
- Face width is broad relative to the torso, about 1.45–1.65 times the maximum torso width. Keep the head silhouette soft and slightly varied by hairstyle; avoid a perfect circle.
- Neck is short and usually partially hidden by clothing. Shoulder slopes and torso shape distinguish identities; limbs use simple tapered forms with rounded joints.
- Hands are compact mitten-like forms with a thumb notch when visible. Add fingers only when the action needs them, at close enough scale to read.
- Feet are low, softly flattened shapes, integrated with footwear; avoid detached bean-like feet.
- Face construction stays inside each character's head silhouette. Ears are small, simple and aligned to the eye/nose axis. Nose is a small warm line or shape, never a large dot that competes with the eyes.

### Face and hair
- Eyes use a compact almond/oval sclera with dark warm outline, iris, pupil, and one small cream highlight. C1 baseline on its source grid: sclera rx 18.5 / ry 23; iris r 9.2; pupil r 5; highlight r 3. Surprise/curiosity may raise sclera ry to 24.5, which is the ceiling for this direction. Do not materially enlarge the eyes.
- Gaze is legible from iris/pupil placement. Eyelid arcs can cover the upper sclera for listening, skepticism, fatigue, or sincerity. Do not depend on eye size alone to carry emotion.
- Brows are independent shapes/lines. Change angle, lift, asymmetry and distance from the lid to carry intent.
- Mouth is a small, readable shape/line that varies among closed, soft smile, open speech, rounded surprise, pressed, and asymmetric states. Use expression scale appropriate to camera distance.
- Blush is optional and restrained: soft warm ellipses around 13 × 6.5 source units at about 0.25 opacity. Freckles are sparse tiny marks, around 2–2.4 units. Neither is a default facial stamp.
- Hair is built from a few connected, readable locks and a clear outer silhouette. Use mass and direction, not dozens of strands. Signature clips, glasses, or ties remain small and secondary.
- Clothing uses clear large shapes, simple collars/necklines, and a limited number of seams. Do not add fabric texture unless the shot needs it.
- Preserve recognizable face, hair silhouette, and signature details across camera distance, pose, expression, and lighting.

## 3. Character identities

All four belong to one drawing system. Their distinctions come from silhouette, hair, facial proportions, outfit cut and one accessory as well as palette. Skin tone is identity data and must remain stable.

| ID | Canonical reference | Stable identity |
|---|---|---|
| male-01 | references/storybook-expressive-chibi-v1/C1/characters/male-01.svg | Medium height, wavy dark-brown hair, relaxed shoulders, teal top with warm ochre detail. |
| male-02 | references/storybook-expressive-chibi-v1/C1/characters/male-02.svg | Slightly taller/narrower frame, swept dark hair, glasses, blue top with ochre detail. |
| female-01 | references/storybook-expressive-chibi-v1/C1/characters/female-01.svg | Compact frame, plum bob, coral top, small gold hair clip. |
| female-02 | references/storybook-expressive-chibi-v1/C1/characters/female-02.svg | Taller/slender frame, tied-up dark hair, olive top, muted lilac signature clip. |

The palette details are recorded in the token file. Do not alter the identity to express an emotion. Expression changes must not change eye spacing, face width, hairline, skin tone, or signature accessories. A later production master may refine anatomy and outfit details, but must maintain the identity anchors above.

## 4. Expression system

The 11 C1 states below are canonical reusable expression recipes. They describe a face and performance, not 11 different character designs. Combine brow, lid, gaze, mouth, head tilt, and body gesture. Intensity 0.0–1.0 controls amplitude; 0.0 is neutral and 1.0 is the strongest readable form. Keep ordinary acting around 0.25–0.7. Use 0.8–1.0 only when story stakes support it.

| Slug | Brows | Lid / eyes | Gaze | Mouth | Optional head / body | Intensity |
|---|---|---|---|---|---|---|
| neutral | relaxed, level | open at rest | forward or scene target | closed, soft | upright, still | 0.0–0.3 |
| listening | inner brow slightly lifted | upper lid relaxed | toward speaker | closed, slight soft curve | slight lean toward speaker | 0.2–0.5 |
| talking | asymmetric, small lift | attentive open | listener or action | small open speech shape | one restrained hand gesture | 0.25–0.65 |
| happy | gently lifted | softly narrowed | toward companion | warm smile | shoulders release | 0.25–0.7 |
| curious | one brow higher | modestly open, never enlarged past token cap | toward new information | small parted or tilted mouth | head tilt 4–10 degrees, lean in | 0.3–0.7 |
| thinking | brows lightly drawn or one raised | upper lid lowered slightly | up, aside, or at object | small closed / asymmetric | hand to chin or pause | 0.25–0.6 |
| awkward | brows lifted unevenly | glance aside | away then back | compressed or hesitant smile | shoulders tuck, small hand movement | 0.25–0.65 |
| skeptical | one brow raised, other level | one lid slightly lowered | direct or side glance | one-sided, closed | slight backward lean | 0.3–0.75 |
| surprised | brows lifted | open; sclera ry at most 24.5 source units | on cause of surprise | small rounded open shape | short recoil; avoid flailing | 0.35–0.8 |
| annoyed | brows lower and draw inward | narrowed, not angry slits by default | at source of friction | pressed or small down curve | crossed arms or turned shoulder when useful | 0.25–0.75 |
| sincere | brows softened, inner ends slightly raised | relaxed, steady | companion or meaningful object | gentle closed smile or small speech | open posture, small nod | 0.2–0.6 |

Canonical expression SVG references are in references/storybook-expressive-chibi-v1/C1/expressions/. Treat their facial drawings as examples, not separate character identities. A production character may need small anatomy adjustments so a state remains readable, but identity landmarks stay fixed.

## 5. Pose vocabulary

Pose changes body action; expression changes face and head acting. They can be combined except where physical action conflicts. Baseline vocabulary:

- standing-neutral
- sitting-neutral
- talking
- listening
- gesturing
- thinking
- looking-away
- leaning-in
- reading
- phone-use
- pointing
- holding-object
- walking

Build poses from a stable skeleton: shoulder line, torso direction, hip direction, elbow/wrist position, support/contact points, and foot/seat relationship. Keep center of gravity plausible. For sitting, show contact with chair/bench and relation to table. For held objects, specify which hand and the contact points. Do not redraw the entire character to add a prop; preserve identity master and attach or compose a hand/prop pose.

Create poses as composable components or deterministic variants in Phase 4. Do not export the full cross product of every character × pose × expression.

## 6. Camera and portrait composition

Every camera type has its own composition. Recompose subject, props, and background for the shot; do not implement a camera test by cropping or uniformly scaling an existing full-scene plate.

The ratios below are composition targets on 1080 × 1920, not platform UI guarantees. Reserve roughly 7% at each side, 7% at top, and 16–18% at bottom for controls/captions. Keep essential facial acting above the lower caption band. Allow shot-specific exceptions only when the action remains readable.

| Shot type | Subject scale and placement | Eye line / head room | Secondary subject and props | Background / foreground |
|---|---|---|---|---|
| establishing / wide | Character group about 40–55% of frame height; scene should establish a place or relationship. | Eye line about 35–43%; head room 6–10%. Do not leave more than roughly 25% blank above heads without a story reason. | Keep table/chairs and one story-relevant object readable. | Show enough environment to locate the scene; purposeful foreground may frame the action. |
| medium two-shot | Pair about 55–68% frame height; bodies and interaction fit. | Shared eye line around 34–42%; 5–8% head room. | Keep character spacing and the object between them clear; neither face should overlap. | Reduce background contrast behind faces. |
| medium single | Main character about 55–70% frame height, occupying the visual center or intentional third. | Eye line 32–42%; 5–8% head room. | Supporting character may be absent, a partial OTS silhouette, or at most 10–15% of the visual area. No equal-size competing face. | Remove competing high-contrast props/decor. |
| close-up | Compose face/head/shoulders specifically; face roughly 38–55% frame width, depending on expression. No full body. | Eye line 35–42%; 6–10% head room. | Show only a hand/prop if it supports the facial beat. | Use quiet value shapes; hair and ears stay inside the frame. |
| reaction close-up | Reaction face about 48–65% frame width. | Direct gaze toward the offscreen cause or a defined eyeline; 5–9% head room. | Exclude other faces. Cause may appear as edge hint only. | Keep cause direction clear; use subdued focus falloff or value grouping, not fake lens blur. |
| insert | Hero prop about 35–60% frame width and 30–50% frame height. | No face eye line; establish screen direction from adjacent shot. | Hand/contact can enter if it clarifies action. No unrelated prop cluster. | Table or surface establishes depth; background detail low. |
| over-shoulder | Listener foreground shoulder about 15–25% width; speaker remains the clear focal plane. | Preserve speaker eye line from prior shot. | Keep only one readable face. | Foreground shoulder may frame but must not cover key hand/object. |
| detail | One meaningful face feature, hand, or prop about 45–65% frame width. | Follow prior eyeline and screen direction. | One hero detail only. | Background is quiet and supports the detail's narrative meaning. |

Maintain screen direction within a continuous exchange. A cut may change axis when the story motivates it and the new geography is clear. Put subtitles in a consistent dedicated band that avoids mouths, hands, and the active prop.

## 7. Background, depth, and interactive space

Backgrounds are authored as layers so characters and StoryGraph props can interact independently:

1. background/base: wall, sky, broad light and color mass;
2. environment-back: window, distant architecture, shelves, landscape;
3. environment-mid: booth, chair backs, counter, plants;
4. interactive-zone: table/surface, seat contact, usable object anchors;
5. foreground: edge framing, nearby table edge, softly simplified occluder;
6. lighting/atmosphere: broad warm light, window glow, sparse haze or texture.

Layers may be SVG groups, separate SVG assets, or renderer-native layers. Keep the implementation composable. Do not bake an interactive book, phone, cup, or other continuity object into a background. A scene may include fixed environment props, but their metadata must label them as environment/decorative and StoryGraph must not pretend they are independently movable.

Use warm storybook shapes with a clear foreground/midground/background contrast. Detail falls with distance: closest interaction gets the sharpest line and contrast; distant decoration uses fewer marks and lower contrast. Keep a clean region behind expressions and text. Scene changes must have spatial motivation.

## 8. Props, decorations, motifs, effects, and overlays

Props use the same warm outline, rounded geometry, limited detail, and soft light as characters. Use a consistent perspective per shot. Favor broad recognizable contours over tiny symbolic details. A prop's default scale should make hand contact plausible; tokens provide reference relationships for the C1 cafe table/book/cup. Highlights and shadow explain volume but remain quieter than the acting face.

- Interactive prop: story object that can be touched, moved, revealed, or reused as continuity (book, phone, cup, note, bag, gift). It has a stable ID, clean silhouette, declared scale and anchor/contact point, and must stay independent of the background.
- Environment prop: fixed scene object such as chair, lamp, menu board, window frame, or shelf. It establishes place and may not become a continuity object without an explicit independently selectable asset.
- Decorative prop: optional non-interactive detail. It must not compete with the story action and must be removable.
- Decoration: scene-specific environmental detail that builds place, such as framed art or a plant. It does not carry an abstract story meaning by itself.
- Motif: a recurring symbol (lightbulb, heart, question mark) with a defined story meaning or callback. Introduce, transform, or resolve it through the story. Never use it as filler.
- Effect: time-based visual treatment such as glow, reveal, focus accent, or motion cue. Prefer renderer/motion primitives. It must point to the action or change attention; do not include random sparks, comic bursts, or shake.
- Overlay: persistent or beat-scoped graphic layer such as a restrained title, chapter marker, or caption. It must respect portrait safe zones and never obscure face, hand, or continuity prop.

Static asset categories are described in the metadata schema. Dynamic effect timing remains part of the renderer/StoryGraph motion contract, not an excuse to put arbitrary animation behavior in an SVG asset.

## 9. Production taxonomy and file layout

New direction assets belong under:

assets/video/storybook-expressive-chibi/
  backgrounds/
  characters/
    male-01/
    male-02/
    female-01/
    female-02/
  props/
  decorations/
  motifs/
  effects/
  overlays/

Folders organize authored files; they do not grant an asset to an agent. Only a validated runtime catalog entry exposed through allowed_assets grants selection. Character folders may contain identity source, shared state components, and canonical manifests; prefer one identity master plus composable states over a flat set of all state combinations.

Category meanings:
- backgrounds: layered location/base/scene assemblies;
- characters: stable human character identity and its composable pose/expression parts;
- props: interactive or fixed object assets;
- decorations: environment dressing with no interactive-story role;
- motifs: story symbols with an explicit narrative meaning;
- effects: reusable visual treatment definition or asset;
- overlays: authored graphic layers such as title/chapter/caption plates.

Runtime mapping must preserve current semantic roles where possible: backgrounds map to background or scenery; characters to character/human_character; props to prop/object_prop; decorations to scenery/environment; motifs to motif/symbol. Effects and overlays require explicit runtime mapping and validation in Phase 4. Motion timing/easing remains compiler data, not taxonomy metadata.

## 10. Asset metadata contract

Use asset-metadata.v1.schema.json as the proposed production manifest contract. Every asset records stable identity, relative source path, library category, runtime role and subject kind, compatible scene IDs, semantic tags, human-readable label/description, art-direction ID/version, usage, depth intent, origin, and license.

Character identity masters record character_id plus supported_poses and supported_expressions. An individually baked state may also carry pose and expression. StoryGraph placement selects one of the declared supported states; it must not change character identity. Interactive props record usage=interactive. Fixed environment and decorative assets declare their actual use.

The catalog is the allowlist. The design reference directory is excluded. Validate paths under assets/video/storybook-expressive-chibi, reject traversal and missing files, and compute catalog fingerprints over manifest plus bytes. Scene compatibility is checked against the runtime scene registry. A metadata label or matching tag never makes an unlisted asset selectable.

## 11. Consistency rules

Do:
- preserve face, hair silhouette, skin tone, accessory and outfit identity across all states;
- follow the token file for colors and line weights;
- compose shots for one action and one focal point;
- keep story-critical props independent and reusable;
- show believable contact between character, seat, table, hand and object;
- use lighting and background detail to guide attention;
- make motifs earn their screen time.

Do not:
- use A2's giant eyes, sticker outlines, mascot heads or B2's older standalone choices unless represented by this approved C1 system;
- vary identity colors or facial landmarks per expression;
- use a single full-scene illustration as every camera distance;
- bake continuity objects into scenery;
- add decorative clutter to hide empty staging;
- treat effects/motifs as generic cute filler;
- add a new character or prop to production without the correct art-direction metadata and runtime catalog approval.

## 12. Phase 4 implementation work

No application code or production catalog is changed in Phase 3. Phase 4 will need the following, after this specification is reviewed:

1. Introduce stable catalog art_direction_id=storybook-expressive-chibi and art_direction_version=1; add validated category and metadata fields while retaining runtime role/subject mappings used by current StoryGraph.
2. Migrate the app's current chibi-human-story ID and old Knowledge pack direction chibi-object-theater to the new versioned direction. Do not mix legacy entries into the new allowlist. Rebuild/approve the catalog mirror and Writer Context from approved production assets.
3. Add a typed character performance object to the renderable placement contract: character asset ID, pose, expression, intensity, optional head_angle, plus any held-object anchor. Validate requested state against the character manifest. Keep identity refs and evidence fields intact; this is a visual/compiler change, not a narrative/pacing change.
4. Resolve identity master + pose/expression components deterministically in the renderer. Keep camera compositions as independently authored shot layouts. Do not pre-bake every character × pose × expression combination.
5. Extend catalog lint to validate schema/version, role-category-subject combinations, character state vocabulary, scene compatibility, safe source paths, asset existence, SVG safety, art-direction mixing, and catalog/render fingerprints. Return actionable field paths on failure.
6. During migration, invalidate or require review for existing StoryGraphs whose catalog/design fingerprints reference either legacy direction. Never silently rewrite an approved graph or READY output.
7. Keep Writer Context's allowed_assets as the only agent-selectable set. Add semantic descriptions and supported character states there only when approved assets are in the catalog.

## 13. Phase 4 starter production asset plan

This is a scoped first library, not a commitment to create every pose/expression export as a separate SVG:

- Characters: four identity masters with matching expression/performance system; shared pose construction for the 13 vocabulary items; initially implement the common neutral, listening, talking, thinking, gesturing, reading, phone-use, leaning-in, and holding-object states where needed. Expression recipes cover the 11 states in section 4. Compose on demand instead of exporting the full cross-product.
- Backgrounds: cafe interior daylight, cafe window/rain, home desk, bedroom/living room, and neutral indoor conversation scene. Each uses reusable depth layers and explicit interaction anchors.
- Props: book, phone, cup, drink glass, coffee pot, laptop, headphones, shoulder bag, note/paper, pen, keys, watch, flower, gift box, chair, table, lamp, window, menu, plate/food. Mark movable story props interactive and furniture/location dressing environment.
- Decorations: wall art, plant, shelf objects, pendant lamp, window dressing, menu lettering and restrained cafe/home set dressing.
- Motifs: lightbulb, question mark, heart, spark/attention mark and connective callback symbol; each needs a declared narrative meaning and restrained drawing.
- Effects: soft focus cue, warm light reveal, gentle emphasis outline, small transition wash; motion behavior is renderer-defined.
- Overlays: unobtrusive chapter label, title card, and caption-safe plate where the current renderer needs authored graphics.

Build a small representative slice per category first, validate character consistency and shot coverage, then expand based on real StoryGraph needs. Do not duplicate objects in backgrounds if they must move independently.

## 14. Open implementation decisions

- Confirm the app-side versioned catalog and character performance contract against the live VideoStory/renderer implementation before Phase 4. The proposed manifest does not replace Writer Context's current response schema or allowed_assets.
- Decide exact layering file format and whether the character compositor emits SVG fragments or deterministic standalone SVG. Keep both decisions behind the existing renderer boundary.
- Define any runtime role for effects/overlays only when real assets and compiler behavior require it; do not widen the runtime enum speculatively.
- Re-measure proportions against approved canonical C1 masters during production cleanup. Reference SVGs are the visual baseline, not a promise that every demo coordinate is final.

## References

- Character identity, expression, and camera references are under references/storybook-expressive-chibi-v1/C1/.
- Numeric tokens: tokens.storybook-expressive-chibi.v1.json.
- Proposed manifest schema: asset-metadata.v1.schema.json.
- Video writing/directing rules point here from ../rules/video-direction.md.
