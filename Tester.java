public class Tester
{
	public static void main(String[] args)
	{
		Play p = new Play();

		try{
			p.run();
		}catch(NullPointerException e)
		{
			System.out.println(e.getMessage()+"; Points will be deducted.");
		}
	}
}