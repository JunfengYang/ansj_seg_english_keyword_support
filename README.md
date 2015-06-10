# ansj_seg_english_keyword_support

English phase dictionary form Wikitionary to support english keyword calculation in ansj_seg.

It's not a very smart implementation. But it's easy to use.

To make the new dictionary work:

In https://github.com/NLPchina/ansj_seg/blob/master/src/main/java/org/ansj/app/keyword/KeyWordComputer.java

Modify:
```java
static {
	POS_SCORE.put("null", 0.0);
	POS_SCORE.put("w", 0.0);
	POS_SCORE.put("en", 1.0);
	POS_SCORE.put("num", 0.0);
	POS_SCORE.put("m", 0.0);
	POS_SCORE.put("nr", 3.0);
	POS_SCORE.put("nrf", 3.0);
	POS_SCORE.put("nw", 3.0);
	POS_SCORE.put("nt", 3.0);
	POS_SCORE.put("l", 0.2);
	POS_SCORE.put("a", 0.2);
	POS_SCORE.put("nz", 3.0);
	POS_SCORE.put("v", 0.2);
	POS_SCORE.put("stop", 0.0);
	POS_SCORE.put("phrase", 5.0);
}
```

Add the "dicForEn.dic" to the default.dic

Didn't calculate each phase score. But still have acceptialbe results.

Ok, Ready to work.

For test:

```java
KeyWordComputer kwc = new KeyWordComputer(10);
String title = "Tintin in Tibet";
String content = "Tintin in Tibet is the twentieth volume of The Adventures of Tintin, the comics series by Belgian cartoonist Hergé. The cartoonist considered it his favourite Tintin adventure and an emotional effort, as he created it while suffering from traumatic nightmares and a personal conflict while deciding to leave his wife of three decades for a younger woman. The comic, serialised from 1958–59 in Tintin magazine, tells of the young reporter Tintin in search of his friend Chang Chong-Chen, whom the authorities claim has died in a plane crash in the Himalayas. Convinced that Chang has survived, Tintin leads his companions across the Himalayas to the plateau of Tibet, along the way encountering the mysterious Yeti. Themes in Hergé's story include extrasensory perception, the mysticism of Tibetan Buddhism (Tibetan monastery pictured), and friendship. Tintin in Tibet has been translated into 32 languages, is highly regarded by critics, and has been praised by the Dalai Lama, who awarded it the Light of Truth Award. The story was a commercial success and was published in book form in 1960; the series itself became a defining part of the Franco-Belgian comics tradition. ";
Collection<Keyword> result = kwc.computeArticleTfidf(title, content);
```

There's a compiled jar base on ansj_seg 2.0.7
