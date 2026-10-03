# ZODIAC CONTENT MEMORY — v9.10

## Mục đích và thứ tự ưu tiên

Đây là nguồn duy nhất cho rule biên tập dùng chung của Zodiac.

Bốn lớp có quyền quyết định nội dung và trải nghiệm:

1. `KNOWLEDGE_CONTEXT` đặt biên claim.
2. `EDITORIAL_DESIGN` chọn insight, distinction và memorable point nằm trong biên đó.
3. `EXPERIENCE_PLAN`, nếu package có, phân vai trải nghiệm cho các narrative beat đã tồn tại; nó không được tạo fact hay tăng narrative depth.
4. `OUTPUT_CONTRACT` / `OUTPUT_TEMPLATE` / `SLIDE_OPTIONS` quyết định cấu trúc kỹ thuật, content slot và giới hạn render.

`VIRAL_OVERLAY`/`VIRAL_FOCUS`, nếu có, chỉ là dữ liệu anchor riêng của package. Mọi nguyên tắc viral/human-touch nằm trong file này; Writer Context không được mang một bộ rule prose thứ hai.

Workflow bắt buộc:

1. RAW IDEA / shared question đã validate
2. Ranh giới evidence
3. Core insight
4. Distinction và memorable point
5. Narrative capacity và progression
5a. Viewer experience / ExperiencePlan nếu package có
6. Naturalness và recognition
7. Viral overlay nếu có
8. Prose rhythm
8b. Voice và anti-AI lexicon
9. Độ dài và format
10. Final validation

Mục 1–7, gồm gate 5a, là editorial gates và phải qua trước khi viết body. Gate fail thì quay về gate sớm nhất chưa đạt; không cứu bằng câu dài hơn, ví dụ thêm, slang, clickbait hoặc paraphrase evidence.

Contract của package quyết định schema, block ID, số slide và giới hạn kỹ thuật. Contract không được nới evidence boundary hay ép tạo claim. Nếu content type bắt buộc đổi câu hỏi hoặc đòi claim evidence không hỗ trợ, báo package conflict; không tự bịa nội dung hoặc âm thầm phá contract.

## 1. RAW IDEA và shared question

`RAW_IDEA` lưu original intent/provenance. Nó không tự động trở thành mệnh đề mà mọi subject trong batch phải chứng minh.

Khi RAW IDEA là một câu hỏi hoặc premise đủ rộng và evidence của scope cùng hỗ trợ, có thể dùng trực tiếp. Khi RAW IDEA chứa một hành vi/đặc điểm hẹp nhưng evidence giữa các subject khác nhau, pipeline phải giữ RAW IDEA làm provenance và tạo `shared_question` trung tính hơn. Writer trả lời shared question bằng evidence riêng của từng subject, không ép wording hẹp của RAW IDEA lên từng cung.

Ví dụ: RAW IDEA nói “các cung tiếp cận trực tiếp và cởi mở”, nhưng evidence của Cự Giải nói lắng nghe/chăm sóc, Sư Tử nói chủ động chú ý/khen ngợi, Xử Nữ nói chân thành/từ tốn. Khi đó câu hỏi dùng để viết phải broadening về “mỗi cung thể hiện và đón nhận sự quan tâm theo cách nào khi tán tỉnh?”, còn RAW IDEA vẫn được giữ để truy provenance.

Format, series, angle, headline và layout chỉ định cách trình bày; chúng không đổi chủ thể, không cấp thêm claim và không phải nguồn evidence.

### Context frame của concept

Ngoài claim về subject, Writer phải giữ đúng **bối cảnh quan hệ** mà concept đang nói tới. Context frame không cấp thêm trait cho cung, nhưng nó quyết định người xem đang hình dung "chuyện gì đang xảy ra giữa những ai".

- Với concept về **ghosting / flirting / dating / compatibility / yêu đương**, không mặc định kể như hai người bạn bình thường nếu product intent đang ở ngữ cảnh tình cảm.
- Nếu package không nói rõ mức độ quan hệ, ưu tiên khung mềm như `đang tìm hiểu`, `đang nói chuyện theo hướng tình cảm`, `hai người đang có gì đó với nhau`; không tự nâng thành `người yêu`, `mối quan hệ lâu dài` hay trạng thái chính thức.
- Context frame được phép xuất hiện trong title/body để người xem hiểu tình huống, miễn nó không làm phát sinh motive, cause, outcome hoặc trait mới.
- Nếu RAW IDEA rộng nhưng series/product intent có context frame rõ, giữ context frame đó nhất quán giữa các subject trong cùng batch.

BLACKLIST ở mục 8b chỉ áp cho **PROSE do Writer viết**; không áp cho `RAW_IDEA`, `shared_question` hay phân tích/editorial metadata ở gate này. Không sửa dữ liệu đầu vào chỉ để né blacklist.

## 2. Ranh giới evidence — claim phải truy ngược được

Mọi insight, distinction, trigger, tension, payoff và hệ quả phải được hỗ trợ bởi context/evidence của package. Evidence đặt biên cho claim, không bắt buộc giữ nguyên câu chữ của nguồn.

BLACKLIST không áp cho evidence, evidence trace hoặc phân tích nội bộ ở mục này. Writer được phép diễn đạt lại evidence bằng từ thường hơn miễn không đổi claim; ví dụ `tiếp cận từ tốn` có thể thành `nói chuyện từ từ`. Ranh giới claim vẫn do toàn bộ §2 quyết định.

Không thêm motive, fear, consequence, trạng thái tâm lý, preference, tần suất, outcome hay hành vi cụ thể nếu package không hỗ trợ. Không biến một diễn giải chiêm tinh thành sự thật đúng với mọi người thuộc cung đó. Tránh tuyệt đối hóa, nhưng cũng không lặp disclaimer/source boilerplate vào prose.

- **Concretization** là diễn đạt một ý evidence đã có bằng từ ngữ hoặc hành vi đời thường dễ hình dung hơn, không đổi nghĩa và không khẳng định nguyên nhân, tần suất hay kết quả mới.
- **Claim expansion** là biến chi tiết minh họa thành sự thật về cung, hoặc thêm motive, fear, điều kiện, tần suất, phản ứng hay hệ quả chưa có trong evidence.

Ví dụ: evidence nói Cự Giải đón nhận sự chăm sóc, quan tâm và gần gũi. “Dễ đón nhận sự quan tâm và gần gũi” vẫn nằm trong evidence. “Sợ bị bỏ rơi nên cần được nhắn mỗi ngày” thêm motive và hành vi cụ thể, nên vượt evidence.

## 3. Core insight — tìm điều đáng nói nhất

Trước prose, viết một câu nội bộ trả lời: **Điều đáng nói nhất mà evidence này cho phép nói về shared question là gì?**

Khi có nhiều proposition độc lập, core insight nên làm rõ relation/distinction giữa chúng mà không tạo fact mới. Ví dụ có thể giữ riêng “cách họ thể hiện” và “kiểu họ dễ đón nhận” nếu evidence support hai lớp đó.

Khi chỉ có **một proposition evidence độc lập**, không bắt buộc tạo một “insight sâu hơn” chỉ để vượt paraphrase. Một beat duy nhất được phép tồn tại nếu nó đủ cụ thể, dễ nhận ra và đáng nói. Nhiệm vụ lúc đó là foreground proposition tốt hơn, không phát minh motive, consequence hoặc contrast giả.

Replaceability Test chỉ dùng để phát hiện độ generic; nếu evidence thật sự không có thêm distinction thì chấp nhận một observation hẹp thay vì thêm stereotype để làm khác cung.

Một slide = một ý rõ. Không dựng cả body từ `nêu preference → giải thích preference → paraphrase preference`.

## 4. Distinction và memorable point

Nếu evidence có nhiều proposition, tìm distinction/relation đáng kể giữa chúng. Có thể là `A khác B`, expression so với preference, điều kiện, giới hạn, tension hoặc reframe. Không ép tạo đối lập nếu evidence không hỗ trợ.

Nếu evidence chỉ có một proposition, memorable point có thể chính là phiên bản ngắn, cụ thể và dễ nhớ nhất của proposition đó. Không bắt buộc thêm lớp phân tích thứ hai.

Trước khi viết body, mỗi slide có một **memorable point**: người xem lướt qua còn nhớ nhận xét gì? Điểm này phải truy được về evidence và không được dùng như giấy phép phóng đại.

Áp dụng Delete Test và Replaceability Test để phát hiện nội dung quá generic, nhưng không dùng hai test này để ép tạo claim mới.

## 5. Narrative capacity và progression — evidence beat không đồng nghĩa slide

Tách rõ ba lớp:

- **Evidence beat** là proposition/claim độc lập được Knowledge hỗ trợ.
- **Narrative beat** là một nhịp biên tập có chức năng riêng trong cách kể, và phải chỉ rõ nó truy về evidence beat nào.
- **Slide** là cách PresentationPlan bố trí một hoặc nhiều narrative beat.

Không dùng số lượng evidence beat làm số slide một cách 1:1. Một evidence beat có thể hỗ trợ hơn một narrative beat khi phần mở rộng chỉ là **concretization** hoặc cách foreground cùng claim, không thêm fact mới. Ví dụ một beat “lắng nghe, chăm sóc và để ý cảm xúc” có thể sinh hai nhịp: (1) observation nêu đặc điểm; (2) micro-behavior hiện thực hóa đặc điểm đó. Cả hai vẫn phải trỏ về cùng evidence beat.

Ngược lại, không được tách một proposition thành nhiều slide chỉ bằng paraphrase. Mỗi narrative beat phải có **editorial function** khác nhau, ví dụ:

- `observation`: nêu điều evidence cho phép nói;
- `concretization`: hiện thực hóa bằng micro-behavior một bước gần;
- `distinction`: đưa lớp evidence thứ hai hoặc relation được hỗ trợ;
- `supported_explanation`, `trigger`, `response`, `correction`: chỉ dùng khi chính evidence/content kind hỗ trợ.

`concretization` không được thêm motive, cause, consequence, frequency, outcome, preference hoặc hành vi xa evidence. Nó phải vượt Camera Test và vẫn đứng vững nếu bỏ mọi diễn giải tâm lý.

### Standalone viability

Bài đăng lẻ một cung cần **ít nhất 3 narrative beat có giá trị**. Đây là yêu cầu về độ sâu kể chuyện, không phải yêu cầu phải có 3 evidence proposition.

- 3+ evidence beat độc lập có thể tạo 3+ narrative beat trực tiếp.
- 2 evidence beat có thể vẫn đủ standalone nếu planner tạo được beat thứ ba bằng concretization hoặc một relation được evidence hỗ trợ.
- 1 evidence beat thường chỉ đủ 1–2 narrative beat; không được bịa nhịp thứ ba để giữ standalone.

Với concept phạm vi 12 cung: nếu sau NarrativePlan có bất kỳ subject nào vẫn không đạt 3 narrative beat, ưu tiên route concept đó sang `carousel_12` để mỗi cung dùng một observation cô đọng. Không route sang carousel chỉ vì `evidence_count < 3`; phải thử NarrativePlan trước.

### Progression test

Nếu đổi thứ tự các narrative beat mà trải nghiệm gần như không đổi, hoặc hai nhịp chỉ paraphrase nhau, progression chưa đạt. Một progression hợp lệ phải có cảm giác đi từ nhận ra → thấy rõ hơn → thêm lớp khác, hoặc một chuỗi semantic tương đương do content kind yêu cầu.

Không mặc định slide cuối phải khen, chê, twist, takeaway hay “mặt trái”. Layout chỉ bố trí narrative; nó không được tạo conclusion mà evidence không support.

Nếu contract kỹ thuật khóa số slide nhiều hơn **narrative capacity**, báo conflict thay vì lặp ý hoặc bịa progression. Nếu contract cho phép thay đổi, chọn số slide theo NarrativePlan rồi mới chọn PresentationPlan/layout.

## 5a. Viewer experience — fact là nguyên liệu, không phải toàn bộ trải nghiệm

Sau NarrativePlan, nếu package có `EXPERIENCE_PLAN`, tách rõ:

- **Narrative beat** trả lời: có thông tin/nhịp biên tập nào thật sự đáng tồn tại?
- **Experience role** trả lời: ở lần vuốt này người xem đang làm gì hoặc nhận được payoff gì?
- **Composition** trả lời: slide cần những content slot semantic nào để thực hiện experience role đó?
- **Layout recipe** chỉ trả lời: các slot được đặt ở đâu và có bao nhiêu không gian.

ExperiencePlan đứng **sau NarrativePlan**. Nó không được tăng `narrative_depth`, thêm narrative index, tạo proposition mới hoặc đổi evidence trace để làm concept “viral hơn”. Nếu narrative chỉ có hai beat thì một mode lý tưởng ba nhịp phải rút còn hai nhịp; không bịa `reframe`, `payoff` hay `twist` để đủ công thức.

Auto mode phải **deterministic theo content kind + narrative shape**, không random để tạo cảm giác đa dạng. Không coi một `recognition_anchor` chỉ lặp lại proposition gốc là tín hiệu đủ để đổi mode. Proposition thuần được phép ở `direct_fact`; concretization/micro-behavior thật **hoặc EvidenceRef được gắn semantic support `observable_behavior`** mới có thể mở `recognition_scene`. Không suy observable behavior bằng độ dài câu, từ khóa hay cảm giác “nghe cụ thể”. `clue_trail` cần nhiều source trace độc lập; `supported_distinction` cần distinction evidence rõ. Nếu pipeline ghi `selection_source` / `selection_reason`, hai field này chỉ giải thích quyết định planner, không phải instruction để Writer phát minh thêm nội dung.

Một experience progression tốt làm cảm giác sau mỗi lần vuốt thay đổi, ví dụ `setup → reveal → reframe`, `scene → reveal → meaning`, `question → clue → payoff`, hoặc một chuỗi tương đương được package hỗ trợ. Nhưng **không bắt buộc gamification**. Khi evidence hẹp hoặc không có clue/distinction đủ mạnh, `direct_fact` là fallback hợp lệ và tốt hơn việc ép A/B, quiz hay hiểu-lầm giả.

Các experience mode chỉ được dùng khi dữ liệu hiện có đủ điều kiện. Đặc biệt:

- `overlooked_signal` cần recognition anchor/concretization đủ cụ thể;
- `recognition_scene` cần observation hoặc micro-behavior có thể hình dung mà không bịa scene fact;
- `zoom_in` cần chi tiết cụ thể để foreground;
- `clue_trail` cần nhiều beat/source trace thật sự cùng trả lời một shared question;
- `supported_distinction` cần distinction được evidence hỗ trợ trực tiếp.

Không tạo distractor, misconception, motive hoặc contrast chỉ để làm người xem đoán.

### Headline là công cụ trình bày, không phải cấu trúc bắt buộc của slide

`title` là identity/metadata của cả post. **Slide 1 luôn có headline để người xem nhận biết nội dung đang xem.** Planner phải chọn composition mở đầu có headline slot trước khi xuất Writer Context; headline slide 1 dùng chính title và title phải fit cap của slot này. Với slide 2 trở đi, visual headline chỉ tồn tại khi composition/OUTPUT_CONTRACT có headline slot.

- Slide 1 bắt buộc có headline slot; dùng chính title làm headline slide 1.
- Nếu contract slide 1 cũ không có headline slot, báo package conflict và yêu cầu Refresh Plan hoặc migration trước khi viết/import. Không tự chèn block ngoài contract. Các composition không có headline chỉ được dùng từ slide 2 trở đi.
- Một slide có thể chỉ có body, callout, hai body hoặc các primitive hợp lệ khác nếu contract chỉ định như vậy.
- Writer không được đổi composition hoặc block type; Writer chỉ điền text vào exact content slot/block contract.

Một slide vẫn cần một ý/narrative purpose rõ, nhưng không cần một dòng “headline” riêng để chứng minh điều đó.

### Viewer Journey Test

Trước prose, hỏi với từng slide: **sau lần vuốt này, trải nghiệm người xem thay đổi ở đâu?**

Nếu nhiều slide liên tiếp chỉ cùng làm một việc kiểu “đọc thêm một câu mô tả”, ExperiencePlan chưa tạo giá trị dù text không trùng nguyên văn. Ngược lại, không được tạo khác biệt trải nghiệm bằng claim mới.

Nếu bỏ một slide mà viewer journey và narrative meaning không mất bước nào, slide đó có khả năng dư. Delete Test cho experience không thay thế Delete Test/evidence validation; nó chỉ kiểm tra presentation value.

Adaptive-fit `continuation` là ngoại lệ: continuation có thể dùng lại cùng narrative index vì nó chỉ tạo thêm không gian cho cùng beat, không phải một experience stage/fact mới.

## 6. Naturalness và recognition — ưu tiên micro-behavior

Nói như một người đang nhận xét hành vi quen thuộc, không như báo cáo phân tích tính cách. Ưu tiên chi tiết **có thể nhìn thấy, nghe thấy hoặc hình dung thành một hành động nhỏ**.

Mỗi slide nên có ít nhất một **reality anchor**. Reality anchor tốt nhất thường là một **micro-behavior**: hành vi nhỏ, cụ thể, dễ nhận ra, cùng bản chất với proposition evidence.

Có bốn mức cần phân biệt:

1. **Evidence restatement** — đúng nhưng chỉ lặp lại trait bằng câu khác; an toàn nhưng thường nhạt.
2. **Micro-behavior illustration** — suy một bước gần từ evidence sang hành vi quan sát được; đây là vùng ưu tiên.
3. **Abstract inference** — suy từ evidence sang ngôn ngữ quan hệ/tâm lý rộng hơn; có thể hợp logic nhưng thường làm câu chung chung, “AI” và khó nhận ra.
4. **Claim expansion** — thêm motive, cause, frequency, outcome, ability hoặc hành vi xa evidence rồi khẳng định nó là trait của subject; không được phép.

### Micro-behavior illustration được phép đi xa tới đâu

Được phép thêm **một bước hiện thực hóa** nếu cả ba điều đúng:

- hành vi là biểu hiện tự nhiên, gần nghĩa của evidence;
- hành vi không cần thêm motive, nguyên nhân hay kết quả để đứng vững;
- câu cụt dạng cảnh được coi là **illustration**, không phải quy luật chắc chắn của cung; nếu cần hedge, ưu tiên độ mềm ở title/caption hoặc dùng `á` / `hà` / `hay` tự nhiên thay vì mở câu bằng `kiểu`. Illustration vẫn phải giữ nguyên ranh giới §2, không thêm claim.

Ví dụ evidence: `lắng nghe, chăm sóc và quan tâm đến cảm xúc`

- Quá sát nguồn: “Cự Giải có cảm tình thường lắng nghe kỹ và để ý cảm xúc của người kia.”
- Chấp nhận: “Bạn kể một chuyện. Họ để ý đoạn làm bạn vui hay khó chịu.”
- **Ưu tiên:** “Nhớ chuyện bạn kể hôm trước. Lần sau gặp còn hỏi: giờ ổn chưa?”

Câu cuối thêm continuity và follow-up chưa có nguyên văn trong evidence, nhưng vẫn là một hiện thực hóa gần của “lắng nghe + chăm sóc + để ý cảm xúc”. Nó được phép vì không thêm motive, verdict hay outcome.

Ngược lại, không phải suy một bước nào cũng hữu ích. Với evidence `trò chuyện chân thành, tiếp cận từ tốn`, các câu như “không đẩy mọi thứ quá nhanh”, “để mối quan hệ tiến từng chút”, “biết chừa khoảng riêng” có thể hợp logic nhưng dễ chuyển sang **relationship abstraction**. Nếu không tìm được micro-behavior thật sự rõ, giữ câu ngắn và sát evidence còn tốt hơn kéo sang loại diễn giải này.

### Camera Test

Trước khi giữ một illustration, hỏi: **nếu quay thành một cảnh ngắn, có thấy hành vi cụ thể gì không?**

- “nhớ chuyện đã kể rồi hỏi lại” → có.
- “dành sự chú ý và khen một điểm vừa nhận ra” → có.
- “không đẩy mối quan hệ quá nhanh” → quá khái quát.
- “tạo kết nối sâu sắc” → trừu tượng.

Camera Test không yêu cầu phải viết scene/POV. Nó chỉ dùng để kiểm tra mức độ cụ thể.

### Không biến illustration thành template

Micro-behavior phải sinh từ evidence của từng subject. Không áp cùng kiểu “nhớ rồi hỏi lại”, “khen đúng lúc”, “cho khoảng riêng” cho nhiều cung chỉ vì chúng nghe đời thường.

Concrete before abstract. Source boilerplate như tên website, “theo chiêm tinh”, “không phải kết luận thực nghiệm” không phải memorable point và không đưa vào prose trừ khi người dùng hỏi về chất lượng nguồn.

## 7. Viral Focus và plugin phân tích — công cụ, không phải nguồn rule

`VIRAL_FOCUS`, nếu có trong Writer Context, chỉ mang **anchor/guidance riêng của package** như recognition anchor, headline anchor, viewer job, open loop hoặc payoff anchor được derive từ EditorialDesign/ExperiencePlan. Nó không chứa rule prose và không cấp thêm claim.

Plugin phân tích content viral có thể được dùng như **phương pháp làm việc** trước khi viết: Quan sát → Phân tích → tìm điểm đặc biệt → Delete/A-B test → đúc kết hướng trình bày. Plugin không phải nguồn rule thứ hai. Mọi đề xuất từ plugin phải quay về file này để kiểm tra evidence boundary trước khi dùng.

Được phép dùng plugin để tìm:
- chi tiết nào nên foreground để người xem dừng lại;
- recognition anchor nào có tính đời thường nhất;
- cách headline rõ hơn hoặc có pattern interrupt;
- behavioral illustration nào làm evidence dễ hình dung hơn.

Không được dùng plugin để cấp thêm fact, motive, cause, consequence, frequency, outcome hay certainty về cung.

Nếu một câu hấp dẫn hơn nhờ **minh họa hành vi**, áp dụng ranh giới ở mục 6. Hedging chỉ dùng khi cần tránh tuyệt đối hóa; không mở câu mặc định bằng “kiểu…”, “dễ hình dung là…” hay “chẳng hạn…”.

Không dùng quota slang, emoji, filler, curiosity gap hay hook score. Tự nhiên quan trọng hơn việc “trông viral”.

Viral analysis từ performance thật có thể cập nhật pattern library, nhưng pattern chỉ tối ưu cách trình bày; pattern không bao giờ trở thành evidence về cung.

## 8. Prose rhythm — viết sau khi gates đạt

Thiết kế title trước body để định vị rõ **toàn post**. Title là post identity/metadata và dùng nguyên title làm headline slide 1. Slide 1 phải có headline slot; nếu contract cũ thiếu slot thì báo conflict để cập nhật plan, không thêm block ngoài contract. Clarity đứng trước hook.

Nếu slide 1 có headline, phần còn lại của slide phải cụ thể hóa chứ không paraphrase headline/title. Nếu slide 1 không có headline, block mở đầu phải thực hiện đúng experience role đã được plan chọn thay vì lặp title bằng một câu khác. Không áp cùng một skeleton câu cho mọi cung.

Không đặt mục tiêu "càng ít câu càng tốt". Một narrative beat có thể mở ra thành 2–4 câu nếu các câu lần lượt làm rõ **cùng một beat**: đặt cảnh, zoom vào chỗ thay đổi, rồi để lại observation đáng nhớ. Các câu bổ sung không được thêm motive, cause, consequence, frequency, outcome hay claim mới.

### Body Depth Test

Sau nháp, hỏi với mỗi body: **nếu chỉ đọc slide này, người xem có biết mình đang nói sâu về điểm nào không?**

- Nếu body chỉ nói lại proposition bằng 1–2 câu khác chữ, chưa đạt depth dù đúng evidence.
- Có thể đào sâu cùng một evidence trace bằng diễn tiến của hành vi, phần còn/phần mất, chi tiết nhìn thấy trong cảnh, hoặc distinction đã có sẵn.
- Body ngắn vẫn hợp lệ khi beat tự nó đã đủ sắc. Không kéo dài để đủ quota.
- Ngược lại, body còn nhiều room trong contract mà chỉ có một câu restatement phải được xem lại trước khi duyệt.

### Show-first checkpoint

Ưu tiên **cho người xem thấy chuyện đang xảy ra trước, rồi mới gọi tên điều đáng nhớ**. Với recognition content, một body tốt thường có nhịp:
`cảnh quen → chỗ thay đổi → chi tiết đọng lại`.

**Concrete before abstract không đồng nghĩa cấm từ khái quát.** Sau khi cảnh/hành vi đã đủ rõ, được phép dùng một từ hoặc cụm evidence-supported như `im lặng`, `chủ động`, `khoảng cách` để **gọi tên payoff/meaning** của phần vừa kể. Từ khái quát chỉ thành vấn đề khi nó thay thế hoàn toàn cho cảnh cụ thể hoặc thêm một lớp nghĩa evidence không support.

Ví dụ tốt: `Bạn nhắn trước thì họ vẫn rep. Nhưng nếu bạn cũng không nhắn nữa, giữa hai đứa gần như chỉ còn sự im lặng.` Phần đầu cho thấy hành vi; `sự im lặng` ở cuối chỉ gọi tên trạng thái đã được cảnh phía trước làm rõ.

### Recognition Reference

Khi evidence cho phép, mỗi narrative beat nên có ít nhất một **reference mà người xem có thể nhận ra ngay từ đời thật**, thay vì chỉ mô tả khái niệm.

Recognition Reference có thể là:

- một câu nhắn ngắn đặt trong ngoặc kép, ví dụ `“ừ thôi nha”`, `“để mai nói tiếp”`, nếu câu đó chỉ dùng để minh họa **thứ đáng lẽ có thể xuất hiện nhưng evidence nói là không có**;
- một hành động nhìn thấy được, như `bạn nhắn trước thì họ mới rep`;
- một trạng thái đối chiếu, như `tin nhắn chưa được trả lời nhưng người đó vẫn online`;
- một vật thể/dấu vết cụ thể, như `đoạn đã gõ vẫn nằm trong ô nháp`.

Reference không được biến thành fact mới. Nó chỉ **neo proposition vào một cảnh hoặc câu chữ quen thuộc**. Nếu phải bịa địa điểm, lịch học, story, seen, emoji, thời gian cụ thể hoặc nội dung tin nhắn mà evidence không support thì bỏ.

Sau mỗi body, hỏi: **có chi tiết nào khiến người xem nói “à, đúng kiểu này” không?** Nếu không có, body có nguy cơ chỉ đang giải thích.

Ví dụ cùng một claim "vẫn trả lời nhưng không còn chủ động": đừng dừng ở câu giải thích. Có thể cho thấy `bạn nhắn thì vẫn rep → chờ họ nhắn trước thì không thấy → phần chủ động đã mất`. Đây vẫn là một evidence trace, không phải ba claim mới.

Không biến checkpoint này thành template cứng. Nếu evidence không có cảnh/contrast đủ rõ, giữ direct fact còn tốt hơn bịa thêm tình huống.

### Semantic Payload Test

Mỗi câu trong body phải làm ít nhất một việc thật:

1. đặt rõ bối cảnh đang xảy ra giữa hai người;
2. cho thấy một hành động/thay đổi có thể hình dung;
3. thêm condition/distinction đã được evidence support;
4. đẩy progression sang lớp tiếp theo.

Cắt câu nếu nó chỉ **bình luận về chính nội dung** mà không thêm gì, kiểu `cảm giác lạ nằm ở đó`, `điểm khác nằm ở đây`, `nghe khó hiểu ở chỗ...`. Những câu này tạo cảm giác có chiều sâu nhưng thực tế không mang thêm thông tin.

Tránh placeholder mơ hồ như `ở chỗ khác`, `đoạn này`, `cái đó` khi người đọc phải đoán chúng đang chỉ cái gì. Nếu chi tiết không thể gọi rõ mà vẫn giữ evidence boundary, bỏ câu đó thay vì giữ một placeholder.

### Natural syntax test

Giọng học sinh vẫn phải là **câu nói tự nhiên**, không phải câu bị bẻ để cố đời thường.

- Tránh các cấu trúc gượng như `người mở lời cứ thành bạn`, `tin nhắn với bạn đứng im`, `bớt rep từ từ`.
- Ưu tiên trật tự nói bình thường: `càng về sau, bạn càng phải nhắn trước`; `tin nhắn bạn gửi không được trả lời`; `đang nói bình thường rồi im luôn`.
- Không dùng một từ văn nói nếu cả cụm xung quanh vẫn vô nghĩa. `rep`, `xong`, `mà` chỉ hữu ích khi câu đang nói một việc rõ.

Tránh cấu trúc lặp `claim → giải thích → tổng kết` trên mọi slide. Không kết bằng câu AI tóm tắt hoặc moral. Kết ở observation/distinction đã được evidence hỗ trợ.

## 8b. Voice và anti-AI lexicon

**REGISTER + VIBE:** như một học sinh đang kể cho bạn cùng bàn nghe về một người — gần, nhẹ, dễ hiểu, có nhịp nói chuyện thật; không mang giọng bài phân tích.

- "Vibe học sinh" đến từ **cách kể**, không phải nhồi teen code. Ưu tiên `đang nhắn`, `nói dở`, `rep`, `để đó`, `online`, `gõ xong lại thôi`; dùng từ mà một bạn lớp 10–12 có thể nói tự nhiên với bạn bên cạnh.
- Cho phép từ nối văn nói như `xong`, `rồi`, `mà`, `tự dưng`, `thế là` khi chúng nối đúng diễn tiến. Không đặt quota và không rải vào mọi câu.
- Ưu tiên cách nói có thể xuất hiện trong giờ ra chơi hoặc chat nhóm: `đang nói tự nhiên im luôn`, `gõ rồi lại thôi`, `vẫn rep mà không mở chuyện trước`. Đây là calibration giọng, không phải template claim.
- Tránh câu nghe "nặng", nhãn hóa hoặc quá văn viết khi có cách nói thường hơn, như `đủ để thành một lời giải thích`, `thứ xuất hiện trong cuộc chat`, `rút khỏi cuộc trò chuyện`, `khép lại cuộc trao đổi`.
- Nếu một câu mô tả được bằng thứ người xem **thấy trên màn hình điện thoại** hoặc **nghe trong một câu kể**, ưu tiên bản đó thay cho danh từ trừu tượng.
- Từ phổ thông, thuần Việt, ưu tiên từ đơn; tránh Hán-Việt trừu tượng khi có cách nói thường ngày rõ hơn.
- Không đặt hard limit số tiếng/câu. Viết theo nhịp nói tự nhiên và đọc thành tiếng; chỉ tách khi câu có hai ý độc lập, khó theo dõi hoặc đọc lên phải lấy hơi ở chỗ không tự nhiên.
- Từ nối như `nhưng`, `trong khi`, `trong lúc`, `rồi`, `xong`, `thế mà` được dùng khi chúng làm mạch kể rõ hơn. Không cấm theo từ khóa; chỉ sửa khi câu bị văn viết, vòng hoặc nhét nhiều claim.
- Các cấu trúc như `không chỉ… mà còn`, `không phải… mà là` không có quota. Chỉ sửa khi cùng một post lặp chúng đến mức thành công thức.
- Không kết slide bằng câu khái quát, moral hoặc câu giải nghĩa lại phần trên.
- Không ép hai slide liền nhau phải khác opening signature hay khác số câu. Chỉ sửa khi cả batch lặp cùng một skeleton khiến các cung nghe như thay tên vào mẫu.
- Câu cụt chỉ dùng khi chủ thể/nghĩa vẫn rõ và nhịp đó thật sự tự nhiên; không cắt câu để né lint. Ưu tiên câu có chủ ngữ, hành động và đối tượng rõ.
- `kiểu` và các hedge văn nói được phép khi đúng ngữ cảnh; không dùng chúng như cách mặc định để làm yếu claim hoặc hợp thức hóa claim vượt §2.
- Không có quota từ đệm theo slide/post. Dùng `á`, `nha`, `luôn`, `liền`, `ghê`, `hà` khi câu nói tự nhiên hơn; bỏ nếu chúng chỉ trang trí hoặc xuất hiện dày tới mức thành diễn.
- Không emoji, không teen code.

**Bảng đổi từ khi evidence cho phép diễn đạt đời thường hơn:**

| Tránh | Ưu tiên |
|---|---|
| `tiếp cận` / `bày tỏ` | `nói chuyện` / `nói ra` |
| `phản hồi` | `trả lời` / `rep` |
| `biểu hiện` / `thể hiện` | `làm` / `cho thấy` |
| `duy trì` / `thiết lập` | `giữ` / `bắt đầu` |
| `gắn kết` / `kết nối` | `gần nhau` / `thân hơn` |
| `trải nghiệm` / `hành vi` | `chuyện` / `việc` / `cách họ làm` |

**BLACKLIST trong prose — nguồn thật duy nhất là `tools/blacklist.txt`**:
`phía họ`, `cảm nhận rõ`, `thể hiện`, `đón nhận`, `điều này cho thấy`, `qua đó`, `nhìn chung`, `tóm lại`, `vì vậy`, `tiếp cận`, `bày tỏ`, `phản hồi`, `biểu hiện`, `duy trì`, `thiết lập`, `gắn kết`, `trải nghiệm`.

Các cụm từng cho output xấu như `cuộc chat`, `câu chốt`, `chuyển sang mục tiêu khác` là **calibration BAD**, không phải từ cấm tuyệt đối. `tương tác`, `sự chú ý`, `kết nối` cũng không bị hard-ban vì đôi khi chúng là cách giữ đúng semantic của evidence; Writer vẫn phải ưu tiên cách nói đời thường hơn khi có bản thay thế tự nhiên.

Danh sách trong Markdown chỉ là bản tóm tắt để người đọc thấy rule; test C3 bắt buộc nó đồng bộ hai chiều với `tools/blacklist.txt`. Blacklist chỉ áp cho prose Writer xuất ra, không áp cho evidence, shared_question hay phân tích. Được phép diễn đạt lại evidence bằng từ thường hơn, nhưng §2 vẫn là biên claim.

**PREFER khi evidence hỗ trợ:** động từ và vật thể nhìn thấy được như `nhắn`, `trả lời`, `hỏi lại`, `nhớ`, `gõ`, `gửi`, `để đó`, `im`, `nói thẳng`, `khen`. Không biến danh sách này thành template hành vi.

**STYLE PASS bắt buộc sau nháp:** soi từng câu/body bằng 8 câu hỏi:
1. Một bạn cùng lớp có thật sự kể câu này như vậy không, hay nó nghe như bài phân tích?
2. Có từ/cụm BLACKLIST không?
3. Câu đang cho thấy chuyện gì xảy ra hay chỉ đang gọi tên/giải thích nó?
4. Câu có semantic payload thật không, hay chỉ bình luận kiểu `điểm lạ nằm ở đây`?
5. Chủ ngữ, hành động và đối tượng có rõ không, hay câu bị gượng chỉ để nghe "đời thường"?
6. Body đã đi đủ sâu vào beat chưa, hay mới dừng ở một câu fact?
7. Có chỗ nào có thể đổi từ nhãn như `cuộc...`, `mục tiêu...`, `câu chốt...` thành hành động nhìn thấy được không?
8. Xóa câu cuối thì slide mất một bước đáng nhớ hay chỉ mất câu tổng kết?

Fail bất kỳ câu hỏi nào thì viết lại hẳn câu đó; không sửa nhẹ bằng đổi vài từ.

## 9. Độ dài, fit và format — theo contract package

Giới hạn chung chỉ là hướng dẫn mặc định: headline tối đa 55 ký tự. Với body, `max_chars` của contract là **trần kỹ thuật, không phải mục tiêu**; viết đủ để beat có cảnh, diễn tiến hoặc distinction đáng nhớ rồi mới dừng. Mốc 225–240 chỉ dùng để đánh giá sức chứa/fit khi pipeline cần, không phải target prose.

Mức sàn bắt buộc của body là **đủ nghĩa và có chiều sâu cho narrative beat**: có hành vi/cảnh, diễn tiến, recognition reference hoặc distinction được evidence hỗ trợ, phù hợp chức năng của block. Không dùng số từ, số câu hay dấu chấm làm bằng chứng rằng body đã đủ sâu. Body/callout ngắn có chủ đích vẫn hợp lệ nếu thực hiện đủ chức năng của nó; một body chính chỉ restate proposition thì phải quay lại Body Depth Test.

Không có hard minimum số học cho body. Tuy vậy, với block có cap khoảng 320–480 ký tự, một body rất ngắn phải qua Body Depth Test: nếu nó chỉ restate evidence thì Writer phải đào sâu **cùng evidence trace**, không được viện cớ anti-AI để cắt nội dung thành vài câu cụt.

Runtime có thể cho body rộng tới 480 ký tự khi geometry thực sự đủ sức chứa. Đây là ceiling, không phải quota phải viết đầy; vùng nhỏ, font lớn hoặc callout giữ cap riêng. Khi tăng sức chứa phải đồng bộ Writer, schema/export/import, Presentation và render QC; không chỉ sửa prompt hoặc nâng cap mà bỏ kiểm tra overflow.

`OUTPUT_CONTRACT`, `OUTPUT_TEMPLATE`, `SLIDE_OPTIONS` quyết định trần, số dòng, số slide, thứ tự và block ID. Contract override giới hạn kỹ thuật chung khi có xung đột; nội dung vẫn phải qua editorial gates.

### Adaptive fit

Giới hạn ký tự của block là **hard fit cap của geometry**, không phải tín hiệu bắt Writer làm ý nghèo đi. Nếu một narrative beat đang có giá trị nhưng recipe/layout chỉ cho vùng body quá hẹp để diễn đạt rõ, pipeline được phép tạo một phương án fit rộng hơn.

Thứ tự ưu tiên:

1. Giữ nguyên evidence trace, NarrativePlan và ExperiencePlan trước khi tối ưu geometry.
2. Với presentation v2, ưu tiên composition/recipe roomier **tương thích cùng experience role**. Không đổi sang `header-body` chỉ vì recipe đó rộng hơn nếu việc đó làm mất semantic composition.
3. Nếu một single-beat slide vẫn bị bó bởi geometry và việc rút ngắn sẽ làm mất micro-behavior/distinction đáng giá, có thể thêm **tối đa một continuation/support slide trong một lần fit**. Continuation dùng cùng narrative index/evidence trace và không được trở thành `reframe`, `payoff` hay claim mới.
4. Với legacy v1 multi-beat recipe, có thể giữ behavior decompress hiện hành để tương thích, miễn beat order và evidence trace không đổi.
5. Fit pressure đánh giá vùng prose thực sự cần không gian; không coi một callout ngắn có chủ đích là lý do kéo dài body.
6. Không tách slide chỉ để đạt quota 225–240 ký tự. Nếu câu ngắn đã đủ rõ và mạnh thì giữ ngắn.
7. Cấm chia một câu/paraphrase thành hai slide. Standalone adaptive fit mặc định không vượt 5 slide; nếu vẫn không fit sau một lần tách, ưu tiên đổi layout/composition hoặc rút prose.

Khi `SLIDE_OPTIONS` có cả base count và base+1 do fit, Writer được chọn base+1 trong preview nếu chất lượng rõ ràng tốt hơn. JSON cuối phải dùng đúng một option đã chọn và giữ nguyên block contract của option đó. Nếu fit bắt đầu từ một package-specific manual layout, quay lại base phải phục hồi đúng base layout đó thay vì làm mất override.

Header dùng sentence case, không ALL CAPS. Không dùng dash làm công cụ cấu trúc câu trong carousel. Tránh cliché rỗng, thuật ngữ niche và nhiều twist trên cùng slide.

## 10. Final validation

Trước khi gửi, xác nhận:

- RAW IDEA được giữ đúng provenance; shared question không ép premise hẹp lên subject không support.
- Context frame của concept được giữ đúng: ghosting/dating không bị kể thành tình bạn thuần túy; đồng thời không tự nâng mức quan hệ vượt dữ liệu.
- Mọi claim truy được về Knowledge.
- EditorialDesign không chứa source boilerplate hoặc instruction meta thay cho insight.
- Nếu chỉ có một evidence beat, không bịa thêm claim để “đủ insight”; concretization chỉ được tạo thêm narrative beat trong cùng claim boundary.
- Nếu có nhiều evidence beat, NarrativePlan giữ được khác biệt thật giữa chúng và mọi narrative beat đều truy được về source evidence.
- ExperiencePlan không tạo thêm narrative beat/fact; mỗi experience stage truy về narrative index hợp lệ, trừ fit continuation dùng lại cùng index có trace rõ.
- Composition thực hiện đúng experience role; layout chỉ đổi geometry. Không ép mọi slide về headline + body.
- Viral Focus/plugin chỉ thay đổi cách foreground, minh họa và gây chú ý; không thay đổi claim.
- Title rõ nội dung ở cấp post; slide 1 bắt buộc có headline bằng title và fit cap của slot. Từ slide 2 trở đi, visual headline chỉ xuất hiện khi contract có headline slot. Block đầu không lặp title/preference bằng nhiều câu khác nhau.
- Mỗi slide có reality anchor đủ cụ thể; ưu tiên micro-behavior vượt qua Camera Test. Behavioral illustration được phép suy một bước gần từ evidence nhưng không thêm motive/cause/outcome/frequency hoặc biến thành relationship abstraction.
- Batch không lặp cùng skeleton chỉ đổi tên cung.
- Body Depth Test đã qua: mỗi slide nói đủ sâu về beat của nó, không dừng ở restatement chỉ vì câu ngắn dễ lint.
- Register đọc thành tiếng vẫn giống một học sinh kể cho bạn nghe; không trượt sang giọng bài phân tích hoặc caption "nặng".
- Số slide khớp NarrativePlan/contract; adaptive fit chỉ được thêm support slide có trace rõ ràng, không còn bắt buộc khớp 1:1 với số evidence beat.
- Writer tự soi từng câu bằng STYLE PASS ở mục 8b; Writer không tự tuyên bố `lint pass`.
- Pipeline/consumer chạy `tools/lint_zodiac.py` trên Writer prose sau draft; nếu lint fail, feed danh sách lỗi lại cho vòng Writer retry trước approval/render.
- Không có skeleton lặp máy móc ở cấp batch; opening giống nhau chỉ là lỗi khi nó làm các slide nghe như cùng một template.
- JSON cuối khớp response contract sau approval flow.

Nếu một mục fail, quay lại gate sớm nhất liên quan. Không dùng chỉnh prose, kéo dài câu, slang, clickbait hoặc ví dụ để che lỗi insight, evidence hay progression.

## Chưa quy định

Hashtag, CTA và emoji trong caption/slide chưa có rule chung. Không tự suy diễn thành giới hạn bắt buộc.


## Calibration nhanh — dùng khi câu vẫn “đúng mà nhạt”

### Cự Giải · evidence: lắng nghe, chăm sóc, để ý cảm xúc

- **Không ưu tiên:** “Cự Giải thường lắng nghe kỹ. Họ để ý cảm xúc của người kia.”  
  Đúng nhưng mới restate evidence.
- **Chấp nhận:** “Bạn kể một chuyện. Họ để ý đoạn làm bạn vui hay khó chịu.”  
  Có cảnh, vẫn còn hơi mô tả.
- **Ưu tiên:** “Nhớ chuyện bạn kể hôm trước. Lần sau gặp còn hỏi: giờ ổn chưa?”  
  Có micro-behavior và continuity; vẫn trong cùng claim boundary.

### Sư Tử · evidence: chủ động chú ý và lời khen

Các hướng “để người kia biết mình đang được chú ý”, “lời khen bật ra khi nhận thấy một điểm hay”, hoặc “người kia cảm nhận rõ mình được để ý hơn” đều **chấp nhận được**, nhưng chưa mặc định là mức tốt nhất. Writer nên tiếp tục tìm micro-behavior cụ thể hơn nếu evidence cho phép, thay vì dừng ở một câu mô tả chung.

### Xử Nữ · evidence: chân thành, tiếp cận từ tốn, tôn trọng riêng tư

Không tự động biến `từ tốn` thành:
- “không đẩy mọi thứ quá nhanh”;
- “để mối quan hệ tiến từng chút”;
- “giữ khoảng cách”;
- “chừa khoảng riêng cho nhau”.

Các câu này dễ trượt sang relationship abstraction hoặc đổi semantic. Nếu chưa tìm được micro-behavior tốt, dùng observation ngắn, cụ thể và sát evidence; không bắt buộc phải có illustration dài.

### Nặng → nhẹ mà vẫn giữ evidence

- BAD: “Có thể họ đã gõ ra điều muốn nói, đủ để thành một lời giải thích. Rồi dòng chữ ấy vẫn nằm trong ô nháp. Cuối cùng thứ xuất hiện trong cuộc chat không phải lời chia tay hay lời chốt nào cả, mà là im lặng.”
- GOOD: “Có khi lời giải thích đã gõ rồi, xong lại để đó. Không gửi. Đoạn chat im luôn, còn tin nhắn vẫn nằm trong bản nháp.”
- BAD đúng claim nhưng dùng nhiều cụm văn viết và dựng câu theo kiểu phân tích. GOOD giữ cùng evidence trace, nhẹ hơn, có cảnh và đọc giống lời kể hơn.

### BAD → GOOD về giọng

- **Cự Giải 1:** BAD “Cự Giải thể hiện sự quan tâm bằng cách lắng nghe và để ý cảm xúc.” → GOOD “Chuyện bạn kể hôm trước, họ nhớ á. Lần sau gặp là hỏi: chuyện đó ổn chưa?” — BAD: từ sách vở; GOOD: chỉ có cảnh.
- **Cự Giải 2:** BAD “Họ không chỉ nghe chuyện gì xảy ra mà còn để ý xem chuyện đó làm bạn vui hay khó chịu.” → GOOD “Bạn kể một chuyện buồn. Họ hỏi lại đúng đoạn làm bạn khó chịu.” — BAD: cấu trúc giải thích; GOOD: một hành động cụ thể.
- **Sư Tử 1:** BAD “Sư Tử thể hiện sự chú ý thông qua lời khen dành cho người kia.” → GOOD “Thấy bạn có điểm hay là khen liền.” — BAD: từ sách vở; GOOD: động từ trực tiếp.
- **Sư Tử 2:** BAD “Sự chú ý của Sư Tử thường đi cùng một lời khen.” → GOOD “Đang nói chuyện, họ bắt đúng một chi tiết rồi khen.” — BAD: danh từ hóa; GOOD: chỉ có cảnh.
- **Xử Nữ 1:** BAD “Xử Nữ nói chuyện chân thành nhưng vẫn tiếp cận từ tốn.” → GOOD “Họ nói chuyện từ từ. Mà nghĩ sao nói vậy hà.” — BAD: ghép hai vế; GOOD: tách thành hai nhịp.
- **Xử Nữ 2:** BAD “Họ thể hiện sự tôn trọng riêng tư của người kia.” → GOOD “Bạn không muốn kể là họ thôi, không hỏi nữa luôn.” — BAD: mô tả khái niệm; GOOD: hiện thực hóa `tôn trọng riêng tư`.

Các cặp trên calibrate **giọng**, không cấp thêm evidence và không phải template câu.

### Nguyên tắc rút ra

**Độ hay không tỷ lệ với độ xa evidence. Độ hay tăng khi câu chuyển evidence thành một micro-behavior dễ nhận ra.**

Ưu tiên: `micro-behavior cụ thể` → `behavioral illustration` → `evidence restatement` → tránh `abstract relational inference`.

## Changelog v9

- Thêm Voice/anti-AI + STYLE PASS vì v8 kiểm soát ý tốt nhưng chưa khóa giọng ở tầng câu.
- Đổi length guidance và hedging vì target 225–240 cùng câu mở “kiểu…” dễ kéo prose dài, mềm và giống template.
- Viết lại calibration/BAD→GOOD vì ví dụ cũ vô tình dạy Writer dùng cấu trúc AI dù vẫn đúng evidence.
- Thêm lint hooks vào Final validation vì naturalness trước đây chủ yếu là lời khuyên, chưa có cơ chế bắt lỗi.
- Thêm `lint_zodiac.py` + `blacklist.txt` + tests vì STYLE PASS cần một kiểm tra tự động, chỉnh được mà không tạo nguồn evidence/rule mới.


## Changelog v9.1

- Khôi phục guard Sư Tử và Xử Nữ — vì v9 đã xóa mất hai calibration guard giúp ngăn micro-behavior trượt khỏi evidence.
- Siết illustration/hedging và bỏ `kiểu…` làm guard — vì hedge không được dùng để hợp thức hóa claim vượt §2.
- Giới hạn blacklist đúng vào Writer prose và cho phép diễn đạt evidence bằng từ thường hơn — vì evidence/shared_question là dữ liệu biên claim, không phải prose để lint.
- Đổi đơn vị độ dài từ “từ” sang “tiếng (âm tiết)” nhưng giữ N=18 — vì tiếng Việt đọc theo nhịp âm tiết; chưa có đủ dữ liệu để tự hạ ngưỡng.
- TODO-TUNE độ dài: v9.1 có 13 câu trong các ví dụ Ưu tiên/GOOD, min 5, median 8, p75 9, p90 11, max 11, mean 7.69 tiếng; đề xuất thử N=12 trên output thật trước khi đổi — vì 18 đang rộng hơn đáng kể so với calibration nhưng chưa được xác nhận.
- Xóa 9 dòng `— / —` và thêm 8b vào workflow — vì placeholder không có evidence không nên nằm trong calibration Writer.
- Làm rõ STYLE PASS của Writer và lint của pipeline — vì Writer tự soi style, còn pass/fail tự động phải do consumer chạy lint và feed lỗi vào retry.
- Điểm tích hợp còn lại: `Zodiac-Controversy-Factory/zodiac_factory/writer.py` tại vòng retry của `OpenCodeWriter.generate` / `generate_batch`; repo Knowledge này không chứa runtime nên PR này không sửa cross-repo — vì không nên tạo integration giả trong repo rule.
- Bổ sung REGISTER + VIBE, filler discipline và bảng đổi từ — vì prose cần đời thường hơn mà không thêm motive/cause/outcome.
- Cập nhật GOOD cho Cự Giải, Sư Tử, Xử Nữ và sửa câu “Nguyên tắc rút ra” — vì ví dụ phải vừa qua Camera Test vừa giữ nguyên evidence boundary.
- Mở rộng blacklist đúng danh sách v9.1 và bắt đồng bộ Markdown ↔ `blacklist.txt` — vì `blacklist.txt` là nguồn thật duy nhất, tránh drift.


## Changelog v9.2

- Bỏ tư duy “2 câu đủ thì dừng” và thêm Body Depth Test — vì anti-AI không được làm narrative beat teo thành một mẩu fact.
- Nới hard cap câu từ 18 lên 24 tiếng, nhưng giữ vùng 8–18 làm nhịp ưu tiên — vì câu nói tự nhiên đôi khi cần giữ hai hành động cùng một beat.
- Cho phép `nhưng` khi contrast tự nhiên; tiếp tục tránh `trong khi` / `trong lúc` trong prose carousel — vì blanket ban làm câu bị cắt vụn và thiếu chất nói.
- Đổi REGISTER + VIBE sang giọng học sinh kể cho bạn cùng bàn, thêm guard chống câu “nặng”/văn viết — vì đời thường không chỉ là bỏ từ blacklist.
- Thêm calibration Nặng → nhẹ và final checks cho body depth/register — vì prose cần vừa qua evidence boundary vừa có chuyện để người xem nhớ.


## Changelog v9.3

- Thêm Show-first checkpoint từ vòng phân tích viral: ưu tiên cảnh quen → chỗ thay đổi → chi tiết đọng lại, thay vì giải thích bằng nhãn.
- Làm rõ "vibe học sinh" là nhịp kể và từ nối văn nói, không phải teen code hay slang quota.
- Thêm `cuộc chat`, `câu chốt`, `chuyển sang mục tiêu khác` vào prose blacklist sau review output thật — vì ba cụm này nghe như người viết đang tóm tắt nội dung hơn là một học sinh đang kể chuyện.
- Mở PREFER cho `xong`, `rồi`, `mà`, `tự dưng`, `thế là` khi chúng nối diễn tiến tự nhiên; không dùng như filler quota.
- STYLE PASS thêm câu hỏi "đang cho thấy hay đang gọi tên" để chống body đúng fact nhưng không có hình ảnh/nhịp kể.


## Changelog v9.4

- Thêm Context frame của concept — vì output ghosting có thể đúng evidence nhưng vẫn sai câu chuyện nếu Writer vô tình kể thành hai người bạn bình thường.
- Với ghosting/flirting/dating, cho phép neo bối cảnh mềm như `đang tìm hiểu` hoặc `đang nói chuyện theo hướng tình cảm` mà không coi đó là claim mới về trait.
- Cấm tự nâng mức quan hệ thành người yêu/chính thức nếu package không hỗ trợ; context chỉ giúp người xem hiểu đúng loại tình huống.


## Changelog v9.5

- Thêm Semantic Payload Test — vì output có thể nghe giống văn nói nhưng vẫn chứa các câu phản ứng rỗng, không thêm cảnh hay nghĩa.
- Thêm Natural syntax test — vì "vibe học sinh" không được phép làm câu sai nhịp tự nhiên như `người mở lời cứ thành bạn` hoặc `tin nhắn với bạn đứng im`.
- Loại placeholder mơ hồ kiểu `ở chỗ khác`, `điểm nằm ở đây` khi referent không rõ.
- STYLE PASS kiểm tra riêng semantic payload và cú pháp tự nhiên, thay vì coi slang/từ nối là bằng chứng rằng câu đã đời thường.


## Changelog v9.6

- Thêm Recognition Reference — vì content đúng evidence nhưng thiếu một câu/chi tiết để người xem đối chiếu với trải nghiệm thật vẫn dễ thành mô tả chung.
- Cho phép dùng câu nhắn mẫu ngắn như một reference khi nó minh họa trực tiếp cho phần có/không có trong evidence; không biến câu mẫu thành fact mới.
- Phân biệt Recognition Reference với visual reference: mục tiêu nằm trong prose, không phải yêu cầu thêm hình minh họa.


## Changelog v9.7

- Gỡ hard lint theo số tiếng/câu; nhịp câu chuyển sang read-aloud + semantic clarity thay vì một ngưỡng số học.
- Gỡ hard-ban `trong khi` / `trong lúc`, opening signature, filler quota, hedge `kiểu` và quota paired-construction — vì các guard này đang phạt chính những móc nối giúp văn nói tự nhiên.
- Câu cụt không còn được khuyến khích để "tạo nhịp"; ưu tiên chủ ngữ + hành động + đối tượng rõ, phù hợp Natural syntax và tài liệu human-touch.
- Thu gọn blacklist cứng: `tương tác`, `sự chú ý`, `kết nối`, `cuộc chat`, `câu chốt`, `chuyển sang mục tiêu khác` chuyển thành context-dependent/calibration, không còn bị lint từ khóa.
- Giữ nguyên §2 evidence boundary, Progression Test, Camera Test, Body Depth, Semantic Payload, Natural Syntax và Recognition Reference.


## Changelog v9.8

- Làm rõ `concrete before abstract` không phải lệnh cấm từ khái quát.
- Cho phép một từ/cụm evidence-supported như `im lặng` làm payoff/meaning sau khi hành vi/cảnh đã đủ rõ.
- Không thêm lint mới; đây là editorial guidance để Writer không né những từ đúng nghĩa rồi sinh câu vòng hoặc gượng.


## Changelog v9.9

- Làm rõ mức sàn là semantic completeness + Body Depth, không phải quota từ/câu; body ngắn không được dùng để né chiều sâu.
- Cho phép ceiling body 480 ký tự khi geometry hỗ trợ; contract cụ thể và render overflow QC vẫn quyết định fit.
- Yêu cầu đồng bộ giới hạn qua Writer, contract, Presentation và renderer; giữ nguyên §2, Camera Test và Progression Test.


## Changelog v9.10

- Bắt buộc headline ở slide 1 để người xem nhận biết nội dung; title phải fit slot mở đầu. Contract cũ thiếu headline cần được migrate trước Writer, không tự thêm block khi export.
- Giữ nguyên §2, Camera Test, Progression Test và các nguyên tắc độ sâu/fit.
