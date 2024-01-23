Apexで五十音の各行を表現するには、Stringのリストを作成し、それに各仮名を追加することができます。以下は、Apexで五十音の「あ行」から「わ行」までのリストを作成する例です。
ーーーーーーーーーーーー
List<String> aRow = new List<String>{'あ', 'い', 'う', 'え', 'お'};
List<String> kaRow = new List<String>{'か', 'き', 'く', 'け', 'こ'};
List<String> saRow = new List<String>{'さ', 'し', 'す', 'せ', 'そ'};
List<String> taRow = new List<String>{'た', 'ち', 'つ', 'て', 'と'};
List<String> naRow = new List<String>{'な', 'に', 'ぬ', 'ね', 'の'};
List<String> haRow = new List<String>{'は', 'ひ', 'ふ', 'へ', 'ほ'};
List<String> maRow = new List<String>{'ま', 'み', 'む', 'め', 'も'};
List<String> yaRow = new List<String>{'や', 'ゆ', 'よ'};
List<String> raRow = new List<String>{'ら', 'り', 'る', 'れ', 'ろ'};
List<String> waRow = new List<String>{'わ', 'を', 'ん'};

// 各リストの内容を出力
System.debug('あ行: ' + aRow);
System.debug('か行: ' + kaRow);
System.debug('さ行: ' + saRow);
System.debug('た行: ' + taRow);
System.debug('な行: ' + naRow);
System.debug('は行: ' + haRow);
System.debug('ま行: ' + maRow);
System.debug('や行: ' + yaRow);
System.debug('ら行: ' + raRow);
System.debug('わ行: ' + waRow);

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
public class JapaneseSorting {

    // 五十音顺序表
    private static Map<String, Integer> orderMap = new Map<String, Integer>{
        'あ'=>1, 'い'=>2, 'う'=>3, 'え'=>4, 'お'=>5,
        'か'=>6, 'き'=>7, 'く'=>8, 'け'=>9, 'こ'=>10,
        // ... 为每个五十音字符添加相应的顺序值
        'ん'=>46
    };

    // 自定义比较器
    private class JapaneseComparator implements Comparable {
        private final String value;

        JapaneseComparator(String value) {
            this.value = value;
        }

        public Integer getOrder(String s) {
            // 获取字符串第一个字符的顺序值
            String firstChar = String.valueOf(s.charAt(0));
            return orderMap.get(firstChar) != null ? orderMap.get(firstChar) : 999;
        }

        public Integer compareTo(Object obj) {
            JapaneseComparator other = (JapaneseComparator)obj;
            Integer order1 = getOrder(this.value);
            Integer order2 = getOrder(other.value);

            if (order1 == order2) {
                // 如果第一个字符相同，则比较整个字符串
                return value.compareTo(other.value);
            }
            return order1.compareTo(order2);
        }
    }

    public static List<String> sortJapanese(List<String> inputList) {
        List<JapaneseComparator> tempList = new List<JapaneseComparator>();
        for (String s : inputList) {
            tempList.add(new JapaneseComparator(s));
        }
        tempList.sort();
        List<String> sortedList = new List<String>();
        for (JapaneseComparator comp : tempList) {
            sortedList.add(comp.value);
        }
        return sortedList;
    }
}



List<String> projects = new List<String>{'さくら', 'あかね', 'たけし', 'こういち'};
List<String> sortedProjects = JapaneseSorting.sortJapanese(projects);

for (String project : sortedProjects) {
    System.debug(project);
}

