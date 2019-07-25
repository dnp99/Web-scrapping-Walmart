package com.example.quiz1.dummy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/**
 * Helper class for providing sample content for user interfaces created by
 * Android template wizards.
 * <p>
 * TODO: Replace all uses of this class before publishing your app.
 */
public class PreferredCountryEngine {

    /**
     * An array of sample (dummy) items.
     */
    public static final List<DummyItem> ITEMS = new ArrayList<DummyItem>();
    /**
     * A map of sample (dummy) items, by ID.
     */
    public static final Map<String, DummyItem> ITEM_MAP = new HashMap<String, DummyItem>();





    private static  int COUNT =PreferedCountrries.country.size();

    private static  List<String> p_cntr =new ArrayList<>();

    static {
        // Add some sample items.


        for (int i = 0; i < COUNT; i++) {

            addItem(createDummyItem(i));
        }

    }

    private static void addItem(DummyItem item) {
        for(int i=0;i<COUNT;i++)
        {
            p_cntr.add(PreferedCountrries.country.get(i).details);
        }

        Collections.sort(p_cntr);
        ITEMS.add(item);
        ITEM_MAP.put(item.id, item);
    }

    private static DummyItem createDummyItem(int position) {
        return new DummyItem(String.valueOf(position+1), "Country " + position, makeDetails(position));
    }



    private static String makeDetails(int position) {

        StringBuilder builder = new StringBuilder();

        builder.append(p_cntr.get(position));

        return builder.toString();
    }

    /**
     * A dummy item representing a piece of content.
     */
    public static class DummyItem {
        public final String id;
        public final String content;
        public final String details;

        public DummyItem(String id, String content, String details) {
            this.id = id;
            this.content = content;
            this.details = details;
        }

        @Override
        public String toString() {
            return content;
        }
    }
}
