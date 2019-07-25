package com.example.quiz1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.quiz1.dummy.DummyContent;
import com.example.quiz1.dummy.PreferedCountrries;

public class MainActivity extends AppCompatActivity


        implements
        AllCountriesFragment.OnListFragmentInteractionListener,
        PreferedCountriesFragment.OnListFragmentInteractionListener{

    public static int  totalcon=0;
    TextView total_cntr;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        total_cntr=findViewById(R.id.et_country);
        totalcon=Integer.parseInt(total_cntr.getText().toString());
    }

    public void saveCountry(View view) {
        AllCountriesFragment allCountries = new AllCountriesFragment();
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.frameLayoutCustomer,allCountries)
                .addToBackStack("allcountries")

                .commit();
    }

    @Override
    public void onListFragmentInteraction(DummyContent.DummyItem item) {
        PreferedCountrries.number+=1;
        PreferedCountrries.country.add(item);
        PreferedCountriesFragment preferedCountriesFragment= new PreferedCountriesFragment();
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.frameLayoutCustomer,preferedCountriesFragment)
                .addToBackStack("p_cntr")
                .commit();
    }

    @Override
    public void onListFragmentInteraction(DummyContent.DummyItem item, int count) {

    }
}
