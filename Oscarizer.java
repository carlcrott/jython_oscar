package modified;

import java.util.List;
import java.util.ArrayList;
import uk.ac.cam.ch.wwmm.oscar.chemnamedict.entities.ChemicalStructure;
import uk.ac.cam.ch.wwmm.oscar.chemnamedict.entities.FormatType;
import uk.ac.cam.ch.wwmm.oscar.chemnamedict.entities.ResolvedNamedEntity;
import uk.ac.cam.ch.wwmm.oscar.Oscar;

public class Oscarizer {

  private String process;

  public Oscarizer() {
    super();
  }

  public void setProcess(String process) {
    this.process = process;
  }

  public String oscarParse() {
    
    Oscar oscar = new Oscar();

    List<ResolvedNamedEntity> entities = oscar.findAndResolveNamedEntities(process);

    ArrayList<String> list = new ArrayList<String>();

    for (ResolvedNamedEntity ne : entities) {
        list.add( ne.getSurface().toString() );

        ChemicalStructure inchi = ne.getFirstChemicalStructure(FormatType.INCHI);
        if (inchi != null) {
            list.add(inchi.toString());
        }
        list.add(" ");

    }

    String listString = "";

    for (String s : list){
      listString += s + "\n";
    }

    return listString;

  }

}


