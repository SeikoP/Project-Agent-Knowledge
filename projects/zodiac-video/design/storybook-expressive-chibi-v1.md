# Storybook Expressive Chibi — Production Design System

Status: approved art-direction foundation; production system specification v1
Art direction ID: storybook-expressive-chibi
Art direction version: 1
Canonical demo: C1 in this document's references directory
Canvas target: portrait, as defined in the token file

This document is the single visual source of truth for production video assets. Runtime Writer Context and its allowed_assets list remain the authority for which concrete assets a StoryGraph may select. This specification defines how approved production assets are made and described; it does not itself add demo references to the runtime catalog.

## 1. Direction and references

Storybook Expressive Chibi combines the scene depth, mature proportions, warm palette, and prop treatment of C1's Storybook base with clearer eye, brow, and mouth acting. Characters remain storybook illustrators' characters: not stickers, mascots, fashion dolls, or children's cartoons.

C1 is the approved foundation, not a freeze of every SVG. The character masters, expression references, and camera plates under references/storybook-expressive-chibi-v1/C1/ are visual evidence for this system. They may be refined when production-quality masters are made, provided they follow these rules. They are demo compositions, not production assets and must never enter allowed_assets.

A2 and B2 are historical exploration only. Do not import their distinctive eye scale, silhouette, color, or rendering choices into production. Old chibi-object-theater and chibi-human-story assets are legacy directions; neither is the source for new assets. Functional pack tags do not define art direction.

The token file is the numeric source of truth for measurable design values and validation thresholds. This document describes visual intent and operating rules; validators and compilers read numeric limits from tokens.storybook-expressive-chibi.v1.json.

## 2. Visual tokens and construction

### Canvas and drawing
Compose for the portrait canvas and reference grid defined in the token file. Production files may use another internal viewBox when export remains deterministic. Place each shot optically according to its composition profile, not automatically at canvas center.

Use the palette, identity colors, line widths, character proportions, facial geometry, shading opacity, and highlight values in tokens.storybook-expressive-chibi.v1.json. The C1 outline is rounded and warm dark ink rather than pure black. Use broad, quiet shading with one clear light direction. Keep paper grain sparse and subtle. Do not use grain to hide poor vector construction. Shadows stay warm and low contrast; avoid hard black shadows, glossy plastic shine, gradients on every object, and noisy texture.

### Character proportions
Measure against the supplied C1 identity references. Numeric proportions are token-controlled. Keep C1's mature small-body / large-head balance; do not push toward A2's oversized head. Use a soft head silhouette that varies through hairstyle instead of a perfect circle. Keep the neck short and usually partially hidden by clothing. Shoulder slopes and torso shape distinguish identities; limbs use simple tapered forms with rounded joints.

Hands are compact mitten-like forms with a thumb notch when visible. Add fingers only when the action needs them and the shot is close enough to read. Feet are low, softly flattened shapes integrated with footwear. Face construction stays inside the head silhouette. Ears are small and aligned to the eye/nose axis. The nose is a small warm line or shape, never a dot that competes with the eyes.

### Face and hair
Eyes use a compact almond or oval sclera with dark warm outline, iris, pupil, and one small cream highlight. Eye geometry and expression bounds come from the token file; do not materially enlarge the eyes. Gaze is legible from iris/pupil placement. Eyelids can cover the upper sclera for listening, skepticism, fatigue, or sincerity. Do not depend on eye size alone to carry emotion.

Brows are independent shapes or lines. Change angle, lift, asymmetry, and distance from the lid to carry intent. Mouth is a small, readable shape or line that varies among closed, soft smile, open speech, rounded surprise, pressed, and asymmetric states. Use expression scale appropriate to camera distance.

Blush and freckles are optional and restrained. Their geometry and opacity come from tokens; neither is a default facial stamp. Hair is built from a few connected, readable locks and a clear outer silhouette. Use mass and direction, not dozens of strands. Signature clips, glasses, or ties remain small and secondary.

Clothing uses clear large shapes, simple collars/necklines, and a limited number of seams. Do not add fabric texture unless the shot needs it. Preserve recognizable face, hair silhouette, skin tone, outfit identity, and signature details across camera distance, pose, expression, and lighting.

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

The C1 expression states are reusable face and performance recipes, not separate character designs. Combine brow, eyelid, gaze, mouth, head tilt, and body gesture while preserving identity landmarks. Numeric intensity profiles and angle bounds are defined in the token file; use intensity to modulate acting, not to scale or distort character identity.

| Slug | Brows | Lid / eyes | Gaze | Mouth | Optional head / body |
|---|---|---|---|---|---|
| neutral | relaxed, level | open at rest | forward or scene target | closed, soft | upright, still |
| listening | inner brow slightly lifted | upper lid relaxed | toward speaker | closed, slight soft curve | slight lean toward speaker |
| talking | asymmetric, small lift | attentive open | listener or action | small open speech shape | one restrained hand gesture |
| happy | gently lifted | softly narrowed | toward companion | warm smile | shoulders release |
| curious | one brow higher | modestly open within token bounds | toward new information | small parted or tilted mouth | token-bounded head tilt, lean in |
| thinking | brows lightly drawn or one raised | upper lid lowered slightly | up, aside, or at object | small closed or asymmetric | hand to chin or pause |
| awkward | brows lifted unevenly | glance aside | away then back | compressed or hesitant smile | shoulders tuck, small hand movement |
| skeptical | one brow raised, other level | one lid slightly lowered | direct or side glance | one-sided, closed | slight backward lean |
| surprised | brows lifted | open within token bounds | on cause of surprise | small rounded open shape | short recoil; avoid flailing |
| annoyed | brows lower and draw inward | narrowed, not angry slits by default | at source of friction | pressed or small down curve | crossed arms or turned shoulder when useful |
| sincere | brows softened, inner ends slightly raised | relaxed, steady | companion or meaningful object | gentle closed smile or small speech | open posture, small nod |

Canonical expression SVG references are in references/storybook-expressive-chibi-v1/C1/expressions/. Treat their drawings as examples, not separate character identities. A production character may need small anatomy adjustments so a state remains readable, but identity landmarks stay fixed.

## 5. Pose vocabulary

Pose changes body action; expression changes face and head acting. They combine unless the physical action conflicts. The baseline vocabulary is defined in the token file and demonstrated by the C1 reference system.

Build poses from a stable skeleton: shoulder line, torso direction, hip direction, elbow/wrist position, support/contact points, and foot/seat relationship. Keep center of gravity plausible. For sitting, show contact with chair/bench and relation to table. For held objects, specify which hand and the contact points. Do not redraw the entire character to add a prop; preserve the identity master and attach or compose a hand/prop pose.

Create poses as composable components or deterministic variants in Phase 4. Do not export the full cross product of every character, pose, and expression.

## 6. Camera and portrait composition

Every camera type has its own composition. Recompose subject, props, and background for the shot; do not implement a camera test by cropping or uniformly scaling an existing full-scene plate.

The camera profiles in the token file are the only numeric source for canvas bounds, safe areas, subject scale, eye line, headroom, prop scale, spacing, overlap, and caption exclusions. These values guide validation and compilation. They are layout targets, not platform UI guarantees. Keep essential facial acting and story-critical objects clear of the caption band.

| Shot type | Composition intent |
|---|---|
| establishing / wide | Establish place and relationship. Use purposeful environment; avoid blank space above the group unless it serves the story. |
| medium two-shot | Keep both characters and their relation readable. Preserve a shared eyeline and make the interactive object between them visible when the story uses it. |
| medium single | Give one character visual priority. Omit the support character or reduce it to a non-competing partial/over-shoulder presence. |
| close-up | Recompose around face, hair, and shoulders. Do not enlarge a full-body composition. Keep the acting readable against a quiet background. |
| reaction close-up | Isolate the reacting face and make gaze direction point toward the offscreen cause. |
| insert | Give one continuity prop the focal position. Show hand contact only when it clarifies action. |
| over-shoulder | Use the foreground shoulder to establish point of view while keeping the speaker, hand, and relevant object clear. |
| detail | Isolate one meaningful face feature, hand, or prop and preserve direction from the adjacent shot. |

Maintain screen direction within a continuous exchange. A cut may change axis when the story motivates it and the new geography is clear. Put subtitles in a consistent dedicated band that avoids mouths, hands, and the active prop.

## 7. Background, depth, and interactive space

Backgrounds are authored as layers so characters and StoryGraph props can interact independently:

- background/base: wall, sky, broad light and color mass;
- environment-back: window, distant architecture, shelves, landscape;
- environment-mid: booth, chair backs, counter, plants;
- interactive-zone: table/surface, seat contact, usable object anchors;
- foreground: edge framing, nearby table edge, softly simplified occluder;
- lighting/atmosphere: broad warm light, window glow, sparse haze or texture.

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

Folders organize authored files; they do not grant an asset to an agent. Only a validated runtime catalog entry exposed through allowed_assets grants selection. Character folders may contain an identity master, declared state components, and a canonical manifest. Compose the selected pose and expression at render time; do not author a file for every state combination.

Semantic category describes what an asset is. runtime_compatibility describes how the current engine can consume it. Store them separately in asset-metadata.v1.schema.json. For the current asset-catalog contract, direct mappings are explicit:

| Semantic category | Current runtime compatibility |
|---|---|
| backgrounds | Direct role background or scenery; subject kind environment. |
| characters | Direct role character; subject kind human_character. |
| props | Direct role prop; subject kind object_prop. |
| decorations | Direct role scenery; subject kind environment. |
| motifs | Direct role motif; subject kind symbol. |
| effects | Unsupported by default; role and subject kind are null. A registered adapter is required before runtime exposure. |
| overlays | Unsupported by default; role and subject kind are null. A registered adapter is required before runtime exposure. |

An adapter mapping must name a registered adapter and its target contract. Never infer runtime role from semantic category, filename, tags, or visual similarity. Do not encode effects as motifs or overlays as scenery by default. Motion timing/easing remains compiler data unless an explicit supported adapter contract says otherwise.

## 10. Asset metadata contract

Use asset-metadata.v1.schema.json as the proposed production manifest contract. Every asset records stable identity, relative source path, semantic category, an explicit runtime_compatibility object, compatible scene IDs, tags, label/description, art-direction ID/version, usage, depth intent, origin, and license. Semantic category is not a runtime role.

For each character identity master, state_components declares:
- pose_components: unique pose state plus SVG component_id and affected body channels;
- expression_components: unique expression state plus SVG component_id and affected face features;
- capabilities: the intensity range and the channels it may affect, plus head-angle bounds and a component_id for the head pivot.

The renderer composes the identity master, one selected pose component, and one selected expression component. Intensity modulates expression amplitude and declared pose motion channels; it never changes identity, proportions, palette, or the selected base pose. head_angle rotates the declared head group around its pivot and is independent of intensity. Numeric ranges come only from the token file. This composes states on demand and does not require a pre-rendered SVG for every combination. A baked-state asset remains possible only when pose and expression are explicit.

The runtime validator checks unique state names, that every declared component_id and head pivot exists in the source SVG, that state values are in the token vocabulary, and that requested intensity/angle stays inside both the token and character capability bounds. Cross-file checks also validate source paths, scene compatibility, art-direction identity, registered adapters, and catalog membership.

The catalog is the allowlist. The design reference directory is excluded. Validate paths under assets/video/storybook-expressive-chibi, reject traversal and missing files, and compute the catalog fingerprint from the canonical manifest and referenced asset bytes. Persist the graph's art-direction ID/version, source catalog fingerprint, and design-token fingerprint. The design-token fingerprint covers the exact token file bytes. Any mismatch from the values used to create the graph sets review required. A label or matching tag never makes an unlisted asset selectable.

## 11. Consistency rules

Do:
- preserve face, hair silhouette, skin tone, accessory, and outfit identity across all states;
- follow the token file for measurable colors, proportions, line values, state bounds, and camera thresholds;
- compose shots for one action and one focal point;
- keep story-critical props independent and reusable;
- show believable contact between character, seat, table, hand, and object;
- use lighting and background detail to guide attention;
- make motifs earn their screen time.

Do not:
- use A2's giant eyes, sticker outlines, mascot heads, or standalone B2 choices unless represented by the approved C1 system;
- vary identity colors or facial landmarks per expression;
- use one full-scene illustration for every camera distance;
- bake continuity objects into scenery;
- add decorative clutter to hide empty staging;
- treat effects or motifs as generic cute filler;
- infer a runtime role from semantic category;
- permit an asset with a different art_direction_id or art_direction_version through normal validation.

Migration and fingerprint rules:
- Legacy graph/catalog directions are not auto-upgraded. An absent or legacy art-direction identity requires explicit migration.
- Any missing, unverifiable, or different graph/catalog/design fingerprint sets review required. Do not compile it as current or promote it to READY until a reviewer approves the new revision.
- READY and otherwise approved outputs are immutable. Migration creates a separately identified graph/output revision; it never rewrites an approved package in place.
- An asset whose art_direction_id or art_direction_version differs from the graph/catalog direction fails validation. Only an explicit migration record may authorize a new revision, with provenance and review.

## 12. Phase 4 implementation work

No application code or production catalog is changed in Phase 3.1. Phase 4 will need the following, after review:

1. Introduce stable catalog art_direction_id=storybook-expressive-chibi and art_direction_version=1. Keep semantic category separate from runtime_compatibility; validate direct mappings against roles the engine actually supports.
2. Migrate the app's current chibi-human-story ID and the old Knowledge pack direction chibi-object-theater through an explicit migration. Never auto-upgrade a legacy graph/catalog, mix legacy assets into the new allowlist, or rewrite approved output.
3. Add a typed character performance object to the renderable placement contract: character asset ID, pose, expression, intensity, optional head_angle, plus any held-object anchor. Validate it against the identity master's declared state_components.
4. Resolve identity master plus one pose and one expression component deterministically in the renderer. Preserve separate, independently authored camera compositions. Do not bake the full state cross product.
5. Add lint for semantic category, runtime_compatibility status/mapping, schema version, registered adapters, state component references, scene compatibility, safe paths, missing assets, SVG safety, direction mixing, and catalog/design fingerprints.
6. Persist graph/catalog/design fingerprints. Any mismatch sets review required. Explicit migration creates a new provenance-linked revision. READY and approved output stays immutable.
7. Keep Writer Context allowed_assets as the sole agent-selectable set. Expose an asset only if runtime compatibility is direct or a registered adapter is approved and available.

## 13. Phase 4 starter production asset plan

This is a scoped first library, not a commitment to create every pose/expression export as a separate SVG:

- Characters: four identity masters with matching expression/performance system; shared pose construction for the baseline vocabulary; initially implement the common neutral, listening, talking, thinking, gesturing, reading, phone-use, leaning-in, and holding-object states where needed. Expression recipes follow the canonical states in section 4. Compose on demand instead of exporting the full cross-product.
- Backgrounds: cafe interior daylight, cafe window/rain, home desk, bedroom/living room, and neutral indoor conversation scene. Each uses reusable depth layers and explicit interaction anchors.
- Props: book, phone, cup, drink glass, coffee pot, laptop, headphones, shoulder bag, note/paper, pen, keys, watch, flower, gift box, chair, table, lamp, window, menu, plate/food. Mark movable story props interactive and furniture/location dressing environment.
- Decorations: wall art, plant, shelf objects, pendant lamp, window dressing, menu lettering and restrained cafe/home set dressing.
- Motifs: lightbulb, question mark, heart, spark/attention mark and connective callback symbol; each needs a declared narrative meaning and restrained drawing.
- Effects: soft focus cue, warm light reveal, gentle emphasis outline, small transition wash; motion behavior is renderer-defined.
- Overlays: unobtrusive chapter label, title card, and caption-safe plate where the current renderer needs authored graphics.

Build a small representative slice per category first, validate character consistency and shot coverage, then expand based on real StoryGraph needs. Do not duplicate objects in backgrounds if they must move independently.

## 14. Open implementation decisions

- Confirm the proposed catalog and character performance contract against the live VideoStory/renderer before Phase 4. This metadata contract does not replace Writer Context's response schema or allowed_assets.
- Decide whether the compositor resolves in-file SVG fragments or a deterministic standalone SVG, behind the existing renderer boundary.
- Add effects/overlays to runtime selection only through an explicit registered adapter or a deliberate engine contract change. Their semantic categories do not imply a runtime role.
- Re-measure C1 masters during production cleanup. Numeric bounds remain in the token file; the references are visual evidence, not a promise that every demo coordinate is final.

## References

- Character identity, expression, and camera references are under references/storybook-expressive-chibi-v1/C1/.
- Numeric tokens: tokens.storybook-expressive-chibi.v1.json.
- Proposed manifest schema: asset-metadata.v1.schema.json (metadata contract 1.1).
- Video writing/directing rules point here from ../rules/video-direction.md.
