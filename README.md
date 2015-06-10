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
