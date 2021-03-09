import java.io.*;
import java.util.*;
import org.json.simple.*;
import org.json.simple.parser.*;
import java. util. Iterator;
import java.io.FileWriter;

public class readJson {
   public static void main(String[] args) {
      int population_size = 4;
      JSONParser parser = new JSONParser();
      try {
         Object obj = parser.parse(new FileReader("population.json"));
         JSONObject population = (JSONObject)obj;
         System.out.println(population);
      for(int i = 0;i<population_size;i++){
        JSONObject individual = (JSONObject) population.get(Integer.toString(i));
        System.out.println(individual);
      }



      JSONObject outPopulation = new JSONObject();
      for(int i = 0; i<population_size;i++){
        JSONObject individual = (JSONObject) population.get(Integer.toString(i));
        outPopulation.put(Integer.toString(i),individual);
      }
      FileWriter file = new FileWriter("outPopulation.json");

      file.write(outPopulation.toJSONString());
      file.flush();

      } catch(Exception e) {
         e.printStackTrace();
      }
   }
}
