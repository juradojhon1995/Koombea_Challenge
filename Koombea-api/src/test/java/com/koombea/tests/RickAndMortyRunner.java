package com.koombea.tests;

import com.intuit.karate.junit5.Karate;

public class RickAndMortyRunner {
    @Karate.Test
    Karate testApi() {
        return Karate.run("RickAndMorty").relativeTo(getClass());
    }
}
